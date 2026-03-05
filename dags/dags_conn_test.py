from airflow.sdk import DAG, chain
import pendulum
import datetime
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_conn_test",
    schedule="0 0 * * *", #분 시 일 월 요일
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"),
    catchup=False, # true 일때 과거 날짜의 DAG도 실행됨 위 start_date에 따라 설정
    #dagrun_timeout=datetime.timedelta(minutes=60), # DAG 실행 시간 제한 60분 넘어가면 실패
    tags=["배쉬", "닥", "오퍼레이터"], #web UI에서 DAG를 태그로 검색할 수 있음
    #params={""} # 아래 Task들에게 공통적으로 넘겨줄 파라미터
) as dag:
    t1 = EmptyOperator(
        task_id="t1",
    )

    t2 = EmptyOperator(
        task_id="t2",
    )

    t3 = EmptyOperator(
        task_id="t3",
    )

    t4 = EmptyOperator(
        task_id="t4",
    )

    t5 = EmptyOperator(
        task_id="t5",
    )

    t6 = EmptyOperator(
        task_id="t6",
    )

    t7 = EmptyOperator(
        task_id="t7",
    )

    t8 = EmptyOperator(
        task_id="t8",
    )

    t1 >> [t2, t3] >> t4 # bash_t1이 끝나야 bash_t2가 실행됨
    t5 >> t4
    [t4, t7] >> t6 >> t8