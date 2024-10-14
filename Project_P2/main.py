# main.py

from valid_data import save_records_to_csv, generate_records
from rogue_data import save_records_to_csv as save_rogue_records_to_csv, generate_rogue_records
from combine_data import combine_data
from data_validation import validate_data  
from uploading_gcs import upload_files  
from loading_bq import load_csv_to_bigquery  

if __name__ == "__main__":
    # Generate valid records
    valid_records = generate_records(9000)  
    save_records_to_csv('valid_data.csv', valid_records)  
    print("Valid data saved to 'valid_data.csv'")

    # Generate rogue records
    rogue_records = generate_rogue_records(1000)  
    save_rogue_records_to_csv('rogue_data.csv', rogue_records) 
    print("Rogue data saved to 'rogue_data.csv'")

    # Combine valid and rogue data
    combine_data()  
    
    # Validate the rogue data and generate transactions.csv
    validate_data('raw_data.csv', 'transactions.csv')  

    # Call the function to upload files to GCS
    bucket_name = 'revproject3'  
    upload_files(bucket_name) 

    # Load the CSV to BigQuery
    dataset_id = 'revproject3'  # BigQuery dataset ID
    table_id = 'transactions'  # BigQuery table ID
    source_uri = 'gs://revproject3/2024/transactions/transactions.csv'  # GCS URI

    load_csv_to_bigquery(dataset_id, table_id, source_uri)  