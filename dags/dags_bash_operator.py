from airflow.sdk import DAG, chain
import pendulum
import datetime
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *", #분 시 일 월 요일
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"),
    catchup=False, # true 일때 과거 날짜의 DAG도 실행됨 위 start_date에 따라 설정
    #dagrun_timeout=datetime.timedelta(minutes=60), # DAG 실행 시간 제한 60분 넘어가면 실패
    tags=["배쉬", "닥", "오퍼레이터"], #web UI에서 DAG를 태그로 검색할 수 있음
    #params={""} # 아래 Task들에게 공통적으로 넘겨줄 파라미터
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2 # bash_t1이 끝나야 bash_t2가 실행됨