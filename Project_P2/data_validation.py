# data_validation.py

import pandas as pd
import random
import numpy as np
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Load the data
def validate_data(input_file='raw_data.csv', output_file='transactions.csv'):
    df = pd.read_csv(input_file)

    ### Handling null values ###

    # Replacing missing Order Id with a fake UUID
    df['Order_id'] = df['Order_id'].apply(lambda x: x if pd.notna(x) else fake.uuid4())

    # Replacing missing Customer Id with a fake UUID
    df['Customer_id'] = df['Customer_id'].apply(lambda x: x if pd.notna(x) else fake.uuid4())

    # Replacing missing Customer Name with a fake name
    df['Customer_name'] = df['Customer_name'].apply(lambda x: x if pd.notna(x) else fake.name())

    # Replacing missing Payment Transaction Confirmation Id with a fake UUID
    df['Payment_transaction_confirmation_id'] = df['Payment_transaction_confirmation_id'].apply(lambda x: x if pd.notna(x) else fake.uuid4())

    
    # List of possible failure reasons
    failure_reasons = [
    'Insufficient funds', 
    'Card expired', 
    'Network Issues', 
    'Fraud Suspicion', 
    'Invalid Payment Method'
    ]

    # Filling missing values using apply and a lambda function
    df['Reason_for_payment_failure'] = df.apply(
        lambda row: "Payment Successful" if row['Payment_success_or_failure'] == 'Y' 
        else (row['Reason_for_payment_failure'] if pd.notnull(row['Reason_for_payment_failure']) 
              else random.choice(failure_reasons)), 
        axis=1
    )



    # Example data structure with countries and cities
    country_cities = {
        'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'UK': ['London', 'Manchester', 'Birmingham', 'Liverpool', 'Leeds'],
        'Germany': ['Berlin', 'Munich', 'Frankfurt', 'Hamburg', 'Cologne'],
        'India': ['Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Chennai'],
        'Canada': ['Toronto', 'Vancouver', 'Montreal', 'Calgary', 'Ottawa']
    }

    # Filling missing Customer_city based on Customer_country
    df['Customer_city'] = df.apply(
        lambda row: random.choice(country_cities[row['Customer_country']]) 
        if pd.isnull(row['Customer_city']) and row['Customer_country'] in country_cities 
        else row['Customer_city'], axis=1
    )


    ### Handling Negative Values ###

    # Select only numeric columns for checking negative values
    numeric_df = df.select_dtypes(include=['number'])

    # Replace negative values with their absolute values
    df[numeric_df.columns] = df[numeric_df.columns].abs()
    

    
    ### Standardization ###
    # Replace 'InvalidDate' with a valid date using Faker
    df['Date_and_time_when_order_was_placed'] = df['Date_and_time_when_order_was_placed'].apply(
        lambda x: x if x != 'InvalidDate' else fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S')
    )
    
    
    # Save the cleaned data
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to '{output_file}'")




