import s3fs

# Connect to s3
def connect_to_s3(access_key, secret_key):
    try: 
        s3 = s3fs.S3FileSystem(
                    anon= False,
                    key= access_key,
                    secret= secret_key)
        return s3
    except Exception as e:
        print(e)


# create bucket
def create_bucket_if_not_exist(s3, bucket):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print(f"{bucket} bucket successfully created!")

        else:
            print(f"{bucket} bucket already exists")
        
    except Exception as e:
        print(e)

# upload file to bucket
def upload_to_s3(s3,file_path, bucket, file_name):
    try:
        s3.put(file_path, bucket+'/raw/', file_name)  # add file in bucker/raw folder of S3
        print(f'{file_name} uploaded successfully to bucket {bucket}!')

    except FileNotFoundError:
        print(f"{file_name} is not available at {file_path}")

