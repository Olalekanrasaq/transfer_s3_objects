import boto3
import pandas as pd
import awswrangler as wr

local_path = 'data/customers-1000.csv'
s3_path = 's3://de-class-bucket/customers'
filename_prefix = 'customer_1000'
aws_profile = 'default'
glue_database = 'my_sample_database'
glue_table = 'customers'

def write_s3_parquet(
        local_path: str, s3_path: str, filename_prefix: str,
        aws_profile: str, glue_database: str, glue_table: str):
    '''
    Write a local csv file to S3 in Parquet format and register it in the Glue Data Catalog.
    '''
    session = boto3.Session(profile_name=aws_profile)
    df = pd.read_csv(local_path)

    wr.s3.to_parquet(
        df=df,
        path=s3_path,
        filename_prefix=filename_prefix,
        boto3_session=session,
        dataset=True,
        mode='overwrite',
        database=glue_database,
        table=glue_table,
        index=False
    )

    print(f"File {local_path} has been written to {s3_path} in Parquet format")

if __name__ == "__main__":
    write_s3_parquet(local_path, s3_path, filename_prefix, aws_profile, glue_database, glue_table)