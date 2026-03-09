from airflow.providers.standard.operators.python import PythonOperator
from airflow import DAG
import pendulum
import datetime
import random

with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *", #분 시 일 월 요일
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"),
    catchup=False, # true 일때 과거 날짜의 DAG도 실행됨 위 start_date에 따라 설정
    tags=["파이썬", "닥", "오퍼레이터"], #web UI에서 DAG를 태그로 검색할 수 있음
) as dag:
    def select_fruit():
        fruit = ["APPLE", "BANANA", "ORANGE", "AVOCADO"]
        rand_int = random.randint(0, 3)
        print(fruit[rand_int])

    py_t1 = PythonOperator(
        task_id="py_t1",
        python_callable=select_fruit, #실행할 함수명
    )

    py_t1