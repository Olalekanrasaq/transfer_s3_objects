import boto3
import os

def get_files_from_bucket(source_profile: str, bucket: str, key: str, file_path: str):
    '''
    Fetches files from the specified S3 bucket and key prefix, 
    and downloads them to the local 'data' directory.

    Args:
        source_profile (str): The name of the source AWS profile to use for authentication.
        bucket (str): The name of the S3 bucket.
        key (str): The key prefix for the objects to fetch.
        file_path (str): The local path where the files will be downloaded.

    '''
    # session = boto3.Session(profile_name='forge-airflow-local')
    session = boto3.Session(profile_name=source_profile)
    s3_client = session.client('s3')

    # Fetch the objects
    response = s3_client.list_objects_v2(
        Bucket=bucket, 
        Prefix=key
        )
    # Extract and print object keys
    keys = [obj['Key'] for obj in response.get('Contents', [])]

    for file_key in keys:
        s3_client.download_file(
            Bucket=bucket,
            Key=file_key,
            Filename=f'{file_path}/{file_key.split("/")[-1]}'
        )
        print(f'Downloaded {file_key} to {file_path}/{file_key.split("/")[-1]}')

def upload_file_to_bucket(dest_profile: str, bucket: str, key: str, file_path: str):
    '''
    Uploads a local file to the specified S3 bucket and key.

    Args:
        dest_profile (str): The name of the destination AWS profile to use for authentication.
        bucket (str): The name of the S3 bucket.
        key (str): The key for the object to upload.
        file_path (str): The local path of the file to upload.
    '''
    session = boto3.Session(profile_name=dest_profile)
    s3_client = session.client('s3')

    files = os.listdir(file_path)

    for file in files:  
        s3_client.upload_file(
            Filename=f'{file_path}/{file}',
            Bucket=bucket,
            Key=f'{key}/{file}'
        )
        print(f'Uploaded {file} to s3://{bucket}/{key}/{file}')