from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.utils.dates import days_ago
from dag_config import TABLE_CONFIG
from datetime import datetime

with DAG(
    "spark_bq_parent",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=True
) as dag:

    for table in TABLE_CONFIG:
        TriggerDagRunOperator(
            task_id=f"trigger_{table}",
            trigger_dag_id="spark_bq_child",
            conf={"table": table}
        )
