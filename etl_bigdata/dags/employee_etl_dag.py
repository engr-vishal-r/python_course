# dags/employee_etl_dag.py
from datetime import datetime, timedelta
import json
import logging
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.operators.dataproc import DataprocSubmitJobOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.utils.trigger_rule import TriggerRule

LOG = logging.getLogger("airflow.task")

# Configuration (move to Airflow Variables / Secret Manager)
PROJECT_ID = Variable.get("gcp_project")
REGION = Variable.get("gcp_region", "us-central1")
GCS_BUCKET = Variable.get("gcs_bucket")
DATAPROC_CLUSTER = Variable.get("dataproc_cluster")
BRONZE_PREFIX = f"gs://{GCS_BUCKET}/bronze/employee/"
SILVER_PREFIX = f"gs://{GCS_BUCKET}/silver/employee/"
BQ_DATASET = Variable.get("bq_dataset")
BQ_TABLE = "dim_employee"  # final SCD2 target table
EXTRACTION_BATCH_DAYS = int(Variable.get("extraction_batch_days", 1))

default_args = {
    "owner": "data-platform",
    "depends_on_past": False,
    "email_on_failure": True,
    "email": ["oncall@example.com"],
    "retry_exponential_backoff": True,
    "retries": 2,
    "max_retry_delay": timedelta(minutes=30),
    "retry_delay": timedelta(minutes=10),
}

with DAG(
    dag_id="employee_etl_pipeline",
    default_args=default_args,
    schedule_interval="0 0 * * *",
    start_date=datetime(2025, 1, 1),
    catchup=False,  # set True if you want automatic catchups
    max_active_runs=1,
    tags=["etl", "employee"],
) as dag:

    def compute_watermark(**ctx):
        """
        Determine incremental watermark. This function is idempotent and stores watermark in Variable.
        Logic:
          - Check Airflow Variable 'employee_last_watermark' else default to 30 days ago.
          - For backfills this DAG run can be passed 'execution_date' to compute watermark.
        """
        last_wm = Variable.get("employee_last_watermark", None)
        if not last_wm:
            # default initial watermark: 30 days ago
            import datetime
            last_wm = (datetime.datetime.utcnow() - datetime.timedelta(days=30)).isoformat()
        # compute new watermark boundary for this run
        import datetime
        run_date = ctx["execution_date"].to_datetime_string()
        # we'll extract for previous day by default
        new_wm = (ctx["execution_date"] - datetime.timedelta(days=0)).isoformat()
        ctx["ti"].xcom_push(key="last_watermark", value=last_wm)
        ctx["ti"].xcom_push(key="new_watermark", value=new_wm)
        LOG.info("Computed watermarks - last: %s, new: %s", last_wm, new_wm)
        return {"last": last_wm, "new": new_wm}

    t0_compute_watermark = PythonOperator(
        task_id="compute_watermark",
        python_callable=compute_watermark,
        provide_context=True,
    )

    # Dataproc job: extractor (connects to source DW and writes Bronze parquet to GCS)
    extractor_job = {
        "reference": {"project_id": PROJECT_ID},
        "placement": {"cluster_name": DATAPROC_CLUSTER},
        "pyspark_job": {
            "main_python_file_uri": f"gs://{GCS_BUCKET}/jobs/extract_employee.py",
            "args": [
                "--gcs_output", BRONZE_PREFIX,
                "--last_watermark", "{{ ti.xcom_pull(task_ids='compute_watermark', key='last_watermark') }}",
                "--new_watermark", "{{ ti.xcom_pull(task_ids='compute_watermark', key='new_watermark') }}"
            ],
        },
    }

    t1_extract = DataprocSubmitJobOperator(
        task_id="extract_to_bronze",
        job=extractor_job,
        region=REGION,
        project_id=PROJECT_ID,
        deferrable=False,
        do_xcom_push=True,
    )

    # Transform job: PySpark job reads Bronze, transforms, writes Silver
    transformer_job = {
        "reference": {"project_id": PROJECT_ID},
        "placement": {"cluster_name": DATAPROC_CLUSTER},
        "pyspark_job": {
            "main_python_file_uri": f"gs://{GCS_BUCKET}/jobs/transform_employee.py",
            "args": [
                "--bronze_path", BRONZE_PREFIX,
                "--silver_path", SILVER_PREFIX,
                "--ingest_date", "{{ ds }}",
            ],
        },
    }

    t2_transform = DataprocSubmitJobOperator(
        task_id="transform_to_silver",
        job=transformer_job,
        region=REGION,
        project_id=PROJECT_ID,
        do_xcom_push=True,
    )

    # BigQuery MERGE job for SCD2 - can be done with BigQueryInsertJobOperator
    scd2_merge_sql = f"""
   MERGE `${PROJECT_ID}.${BQ_DATASET}.${BQ_TABLE}` T
USING (
    SELECT * EXCEPT(rn)
    FROM (
        SELECT *, 
        ROW_NUMBER() OVER(PARTITION BY employee_id ORDER BY ingest_ts DESC) rn
        FROM `${PROJECT_ID}.${BQ_DATASET}.staging_employee`
    )
    WHERE rn = 1
) S
ON T.employee_id = S.employee_id AND T.is_current = TRUE

-- SCD2: Change detected
WHEN MATCHED AND T.hash <> S.hash THEN
  UPDATE SET 
      T.is_current = FALSE,
      T.effective_to = S.ingest_ts
      
-- New employee or first version
WHEN NOT MATCHED BY TARGET THEN
  INSERT (employee_id, name, dept, effective_from, effective_to, is_current, hash)
  VALUES (S.employee_id, S.name, S.dept, S.ingest_ts, TIMESTAMP("9999-12-31"), TRUE, S.hash);
    """

    t3_load_bq = BigQueryInsertJobOperator(
        task_id="scd2_merge_to_bq",
        configuration={
            "query": {"query": scd2_merge_sql, "useLegacySql": False}
        },
    )

    def finalize(**ctx):
        # push new watermark after successful run (idempotent update)
        new_wm = ctx["ti"].xcom_pull(task_ids="compute_watermark", key="new_watermark")
        Variable.set("employee_last_watermark", new_wm)
        LOG.info("Updated employee_last_watermark to %s", new_wm)
        return new_wm

    t4_finalize = PythonOperator(
        task_id="finalize",
        python_callable=finalize,
        provide_context=True,
        trigger_rule=TriggerRule.ALL_SUCCESS,
    )

    # DAG dependencies
    t0_compute_watermark >> t1_extract >> t2_transform >> t3_load_bq >> t4_finalize
