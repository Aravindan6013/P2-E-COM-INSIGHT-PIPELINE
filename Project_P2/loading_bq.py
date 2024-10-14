# loading_bq.py


"""from google.cloud import bigquery
import os
from google.api_core.exceptions import GoogleAPIError

# Set the environment variable for Google Cloud authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Project_P2\revproject-437603-5ad55c4b206c.json'

def load_csv_to_bigquery(dataset_id, table_id, source_uri):
    try:
        # Initialize a BigQuery client
        client = bigquery.Client()

        # Configure the load job
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,  # Skip header row if your CSV file has headers
            autodetect=True,      # Automatically detect schema
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,  # Overwrite table data
        )

        # Define the table reference
        table_ref = client.dataset(dataset_id).table(table_id)

        # Start the load job
        load_job = client.load_table_from_uri(
            source_uri,
            table_ref,
            job_config=job_config
        )

        # Wait for the job to complete
        load_job.result()

        print(f"Loaded {load_job.output_rows} rows into {dataset_id}:{table_id}.")
    
    except GoogleAPIError as e:
        print(f"An error occurred: {e}")
"""

        
from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPIError

def load_csv_to_bigquery(dataset_id, table_id, source_uri):
    try:
        # Initialize a BigQuery client
        client = bigquery.Client()

        # Configure the load job
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,  # Skip header row if your CSV file has headers
            autodetect=True,      # Automatically detect schema
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,  # Overwrite table data
        )

        # Define the table reference
        table_ref = client.dataset(dataset_id).table(table_id)

        # Start the load job
        load_job = client.load_table_from_uri(
            source_uri,
            table_ref,
            job_config=job_config
        )

        # Wait for the job to complete
        load_job.result()

        print(f"Loaded {load_job.output_rows} rows into {dataset_id}:{table_id}.")
    
    except GoogleAPIError as e:
        print(f"An error occurred: {e}")


