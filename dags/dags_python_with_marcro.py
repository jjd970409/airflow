from airflow import DAG
import pendulum
from airflow.decorators import task

with DAG(
    dag_id="dags_python_with_macro  ",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2026, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    @task(task_id="task_using_macros",
          templates_dict={'start_date' :  '{{ (data_interval_end.in_timezone("Asia/Seoul") + macros.dateutil.relativedelta.relativedelta(months= -1,days=1)) | ds }}',
                          'end_date' : '{{ (data_interval_end.in_timezone("Asia/Seoul").replace(day = 1) + macros.dateutil.relativedelta.relativedelta(days= -1)) | ds }}'
            }
    )
    def get_datetime_macro(**kwargs):
        templates_dict = kwargs['templates_dict'] or {}
        if templates_dict:
            start_date = templates_dict.get('start_date') or 'No start_date'
            end_date = templates_dict.get('end_date') or 'No end_date'
            print(f"start_date: {start_date}")
            print(f"end_date: {end_date}")
