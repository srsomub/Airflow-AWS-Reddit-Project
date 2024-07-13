from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import os, sys


 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.aws_s3_pipeline import local_to_s3_pipeline


default_args = {
    'owner': 'srsomub',
    'start_date': datetime(2023, 10, 22),
}
 
file_postfix = datetime.now().strftime("%Y%m%d")


with DAG(
    dag_id= 'ETL_Reddit_Pipeline',
    default_args= default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline'] 
) as dag:
    

    # extract data from reddit
    extract = PythonOperator(
        task_id='reddit_extraction',
        python_callable=reddit_pipeline, 
 
        op_kwargs={                          
            'file_name': f'reddit_{file_postfix}',
            'subreddit': 'dataengineering',
            'time_filter': 'day',
            'limit': 100              # get 100 subreddit post per day
        }
    )

    # upload data to AWS S3
    upload_to_s3 = PythonOperator(
        task_id = 'local_to_s3',
        python_callable= local_to_s3_pipeline
    )


    extract >> upload_to_s3
