from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime, timedelta
import pendulum

# IST Timezone
ist = pendulum.timezone("Asia/Kolkata")

def dag_1_task():
    print("Running dag_1 logic")
    # raise Exception("Force failure")  # Uncomment to test failure

def decide_next_task(ti):
    state = ti.get_dagrun().get_task_instance("dag_1").state
    
    if state == "success":
        return "dag_3"
    else:
        return "dag_2"

with DAG(
    dag_id="conditional_flow_dag",
    start_date=datetime(2026, 2, 28, tzinfo=ist),
    schedule="0 3 * * *",  # 3 AM daily IST
    catchup=False,
    default_args={
        "retries": 3,
        "retry_delay": timedelta(minutes=5),
    }
) as dag:

    dag_1 = PythonOperator(
        task_id="dag_1",
        python_callable=dag_1_task
    )

    dag_2 = EmptyOperator(
    task_id="dag_2",
    trigger_rule=TriggerRule.ONE_FAILED
)

dag_3 = EmptyOperator(
    task_id="dag_3",
    trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS
)

dag_1 >> [dag_2, dag_3]
dag_2 >> dag_3