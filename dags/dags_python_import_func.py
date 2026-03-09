from airflow.providers.standard.operators.python import PythonOperator
from airflow import DAG
import pendulum
import datetime
from common.common_func import get_sftp

with DAG(
    dag_id="dags_python_import_func",
    schedule="30 6 * * *", #분 시 일 월 요일
    start_date=pendulum.datetime(2026, 3, 9, tz="Asia/Seoul"),
    catchup=False, # true 일때 과거 날짜의 DAG도 실행됨 위 start_date에 따라 설정
) as dag:
    
    task_get_sftp = PythonOperator(
        task_id="task_get_sftp",
        python_callable=get_sftp, #실행할 함수명
    )

    task_get_sftp