from utils.constant import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME
from etls.aws_s3_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3


def local_to_s3_pipeline(ti):  
    file_path = ti.xcom_pull(task_ids='reddit_extraction', key='return_value')


    # function to establish connection with aws
    s3= connect_to_s3(AWS_ACCESS_KEY, AWS_SECRET_KEY)

    # function to check if bucket exists or not
    create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)

    # upload local csv file to s3 bucket
    file_name = file_path.split('/')[-1]
    upload_to_s3(s3,file_path, AWS_BUCKET_NAME, file_name)



