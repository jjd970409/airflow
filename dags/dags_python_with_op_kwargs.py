from airflow import DAG
import pendulum
import datetime
from airflow.providers.standard.operators.python import PythonOperator
from common.common_func import regist2

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2026, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    regist2_t1 = PythonOperator(
        task_id="regist2_t1",
        python_callable=regist2,
        op_args=["홍길동", "남자", "kr", "seoul"],
        op_kwargs={"email": "hong@example.com", "phone": "010-1234-5678"}
    )

    regist2_t1