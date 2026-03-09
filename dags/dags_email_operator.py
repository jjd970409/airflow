import pendulum
from airflow import DAG
from airflow.providers.smtp.operators.smtp import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *", #분 시 일 월 요일
    start_date=pendulum.datetime(2026, 3, 1, tz="Asia/Seoul"),
    catchup=False, # true 일때 과거 날짜의 DAG도 실행됨 위 start_date에 따라 설정
    tags=["이메일", "닥", "오퍼레이터"], #web UI에서
) as dag:
    send_email_task = EmailOperator(
        task_id="send_email_task",
        conn_id="conn_smtp_gmail", # Airflow Connection에 등록한 SMTP 서버의 Connection ID
        to="jjw9704@naver.com", # 수신자 이메일 주소
        subject="Airflow 성공 메일",
        html_content="<h3>Airflow DAG이 성공적으로 실행되었습니다!</h3>", # 이메일 본문 내용 (HTML 형식)
    )