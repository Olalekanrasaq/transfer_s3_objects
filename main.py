import os
from dotenv import load_dotenv
from transfer_s3_file import get_files_from_bucket, upload_file_to_bucket

load_dotenv()

source_profile = os.getenv('SOURCE_PROFILE')
dest_profile = os.getenv('DEST_PROFILE')
source_bucket = os.getenv('SOURCE_BUCKET')
dest_bucket = os.getenv('DEST_BUCKET')
source_key = os.getenv('SOURCE_KEY')
dest_key = os.getenv('DEST_KEY')
file_path = os.getenv('FILE_PATH')

def main(): 
    get_files_from_bucket(source_profile, source_bucket, source_key, file_path)
    upload_file_to_bucket(dest_profile, dest_bucket, dest_key, file_path)

if __name__ == "__main__":
    main()
