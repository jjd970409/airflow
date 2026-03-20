from airflow import DAG
from airflow.decorators import task
from airflow.providers.standard.operators.python import PythonOperator
import pendulum
import datetime

with DAG(
    dag_id="dags_python_template",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2026, 3, 10, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    def python_function(start_date, end_date, **kwargs):
        print(f"start_date: {start_date}")
        print(f"end_date: {end_date}")

    python_t1 = PythonOperator(
        task_id="python_t1",
        python_callable=python_function,
        op_kwargs={
            "start_date": "{{ ds }}",
            "end_date": "{{ next_ds }}",
        },
    )

    @task(task_id="python_t2")
    def python_function2(**kwargs):
        print(kwargs)
        print(kwargs.get("ds"))
        print(kwargs.get("next_ds"))
        print(str(kwargs.get("data_interval_start")))
        print(str(kwargs.get("data_interval_start")))
        print(str(kwargs.get("ti")))