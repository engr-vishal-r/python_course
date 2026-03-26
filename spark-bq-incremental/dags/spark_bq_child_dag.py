from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import DataprocCreateBatchOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryInsertJobOperator,
    BigQueryCheckOperator
)
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime, timedelta
from dag_config import *
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator

def extract_conf(**ctx):
    table = ctx["dag_run"].conf["table"]
    ctx["ti"].xcom_push(key="table", value=table)

def notify_sla(context):
    SlackWebhookOperator(
        task_id="slack_alert",
        http_conn_id="slack_webhook",
        message=f"""
        🚨 SLA Breach Alert
        DAG: {context['dag'].dag_id}
        Task: {context['task_instance'].task_id}
        Execution Date: {context['execution_date']}
        Table: {context['dag_run'].conf.get('table')}
        """,
    ).execute(context=context)
    
with DAG(
    dag_id="spark_bq_child",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=True,
    dagrun_timeout=timedelta(hours=2),
    sla_miss_callback=notify_sla,
    default_args={
        "email": ["engr.vishal.r@gmail.com"],
        "email_on_failure": True,
        "retries": 1,
    }
) as dag:

    get_conf = PythonOperator(
        task_id="get_conf",
        python_callable=extract_conf,
    )

    spark_job = DataprocCreateBatchOperator(
        task_id="spark_transform",
        project_id=PROJECT_ID,
        region=REGION,
        sla=timedelta(minutes=60),
        batch={
            "pyspark_batch": {
                "main_python_file_uri": SPARK_MAIN,
                "args": [
                    "--table", "{{ ti.xcom_pull(key='table') }}",
                    "--execution_date", "{{ ds }}",
                ],
            },
            "environment_config": {
                "execution_config": {
                    "service_account": DATAPROC_SA
            }
        }
    }
)

    load_to_staging = GCSToBigQueryOperator(
        task_id="load_to_staging",
        bucket="bucket",
        source_objects=[
            "temp/{{ ti.xcom_pull(key='table') }}/*.parquet"
        ],
        destination_project_dataset_table=
            "analytics.{{ ti.xcom_pull(key='table') }}_staging",
        source_format="PARQUET",
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
    )

    # ---------------- DQ CHECKS ---------------- #

    dq_row_count = BigQueryCheckOperator(
        task_id="dq_row_count",
        sql="{% include 'sql/dq/trips_row_count.sql' %}",
        use_legacy_sql=False,
    )

    dq_pk_null = BigQueryCheckOperator(
        task_id="dq_pk_null",
        sql="{% include 'sql/dq/trips_pk_null.sql' %}",
        use_legacy_sql=False,
    )

    dq_duplicates = BigQueryCheckOperator(
        task_id="dq_duplicates",
        sql="{% include 'sql/dq/trips_duplicates.sql' %}",
        use_legacy_sql=False,
    )

    dq_freshness = BigQueryCheckOperator(
        task_id="dq_freshness",
        sql="{% include 'sql/dq/trips_freshness.sql' %}",
        use_legacy_sql=False,
    )

    # ---------------- BACKUP ---------------- #

    backup_partition = BigQueryInsertJobOperator(
        task_id="backup_partition",
        configuration={
            "query": {
                "query": """
                CREATE OR REPLACE TABLE analytics.trips_backup
                PARTITION BY DATE(updated_at)
                AS
                SELECT *
                FROM analytics.trips
                WHERE DATE(updated_at) = DATE('{{ ds }}');
                """,
                "useLegacySql": False,
            }
        },
        location="US",
    )

    # ---------------- MERGE ---------------- #

    merge_to_final = BigQueryInsertJobOperator(
        task_id="merge_to_final",
        configuration={
            "query": {
                "query": "{% include 'sql/merge_trips.sql' %}",
                "useLegacySql": False,
            }
        },
        location="US",
    )

    # ---------------- ROLLBACK ---------------- #

    rollback_partition = BigQueryInsertJobOperator(
        task_id="rollback_partition",
        configuration={
            "query": {
                "query": """
                DELETE FROM analytics.trips
                WHERE DATE(updated_at) = DATE('{{ ds }}');

                INSERT INTO analytics.trips
                SELECT *
                FROM analytics.trips_backup
                WHERE DATE(updated_at) = DATE('{{ ds }}');
                """,
                "useLegacySql": False,
            }
        },
        trigger_rule=TriggerRule.ONE_FAILED,
        location="US",
    )

    # ---------------- DEPENDENCIES ---------------- #

    get_conf >> spark_job >> load_to_staging

    load_to_staging >> [
        dq_row_count,
        dq_pk_null,
        dq_duplicates,
        dq_freshness
    ] >> backup_partition >> merge_to_final

    # rollback listens to everything after backup
    [
        backup_partition,
        merge_to_final
    ] >> rollback_partitionsla=timedelta(minutes=60)
