# uploading_gcs.py


"""import os
from google.cloud import storage

# Set the environment variable for Google Cloud authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Project_P2\revproject-437603-5ad55c4b206c.json'

def upload_to_gcs(local_file_path, bucket_name, destination_blob_name):
    # Check if the local file exists
    if not os.path.isfile(local_file_path):
        print(f"File not found: {local_file_path}")
        return

    # Initialize a Google Cloud Storage client
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    # Create a new blob and upload the file's content
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(local_file_path)

    print(f'File {local_file_path} uploaded to {destination_blob_name}.')

def upload_files(bucket_name):
    # Define the file paths for the files to upload
    local_file_path_1 = r'C:\Project_P2\transactions.csv'  # Path to the first file
    destination_blob_name_1 = '2024/transactions/transactions.csv'  # GCS path for the first file

    # Call the upload function for the first file
    upload_to_gcs(local_file_path_1, bucket_name, destination_blob_name_1)

    # Define the file paths for the second file
    local_file_path_2 = r'C:\Project_P2\raw_data.csv'  # Path to the second file
    destination_blob_name_2 = '2024/transactions/raw_data.csv'  # GCS path for the second file

    # Call the upload function for the second file
    upload_to_gcs(local_file_path_2, bucket_name, destination_blob_name_2)
"""
import os
from google.cloud import storage

def upload_to_gcs(local_file_path, bucket_name, destination_blob_name):
    # Check if the local file exists
    if not os.path.isfile(local_file_path):
        print(f"File not found: {local_file_path}")
        return

    # Initialize a Google Cloud Storage client
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    # Create a new blob and upload the file's content
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(local_file_path)

    print(f'File {local_file_path} uploaded to {destination_blob_name}.')

def upload_files(bucket_name):
    # Define the file paths for the files to upload
    local_file_path_1 = r'C:\Project_P2\transactions.csv'  # Path to the first file
    destination_blob_name_1 = '2024/transactions/transactions.csv'  # GCS path for the first file

    # Call the upload function for the first file
    upload_to_gcs(local_file_path_1, bucket_name, destination_blob_name_1)

    # Define the file paths for the second file
    local_file_path_2 = r'C:\Project_P2\raw_data.csv'  # Path to the second file
    destination_blob_name_2 = '2024/transactions/raw_data.csv'  # GCS path for the second file

    # Call the upload function for the second file
    upload_to_gcs(local_file_path_2, bucket_name, destination_blob_name_2)
