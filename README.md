# Transfer S3 Objects between two AWS accounts

This repository manages the transfer of s3 objects from a source AWS bucket (with read permission) to a destination bucket (with write permission).

The workflow leverage a local staging of the source s3 objects and then uploading to the destination bucket. 

# How to use

- Ensure you have an IAM access and secret key cofigure for the source AWS account with at least read permission to S3 bucket objects. Set it up on your local terminal with `aws configure --profile source-profile`
- Similarly, configure the destination IAM account with a write permission to s3 buckets. `aws configure --profile dest-profile`
- Create a `.env` file to store the functions parameter. These include:

```
SOURCE_PROFILE=<aws_source_profile_configure>
DEST_PROFILE=<aws_destination_profile_configure>
SOURCE_BUCKET=<source_s3_bucket>
DEST_BUCKET=<destination_s3_bucket>
SOURCE_KEY=<source_s3_object_key>
DEST_KEY=<destination_s3_object_key>
FILE_PATH=<local_file_path_for_staging>
```
- Create a python virtual environment and activate it (Optional, but necessary to avoid package conflict).
- Run `pip install -r requiremnents.txt` to install required packages.
- Run `python main.py` to execute the workflow.