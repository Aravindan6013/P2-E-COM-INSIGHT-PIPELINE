# E-Com Insight Pipeline

## Overview
The *E-Com Insight Pipeline* is a comprehensive data engineering project designed to streamline the process of generating, cleansing, analyzing, and visualizing E-Commerce data. The goal is to equip the Analytics team with actionable insights derived from large-scale data, enabling stakeholders to make well-informed business decisions. The pipeline leverages Google Cloud Storage (GCS) and BigQuery for data storage and processing, with dynamic visualizations created using Looker Studio.

## Project Components

### Objective
1. *Data Generation*: 
   - Develop a Python program to generate CSV data adhering to the specified E-Commerce data schema. This data simulates real-world transactions and includes rogue records to enhance the robustness of the analysis.
   
2. *Exploratory Data Analysis (EDA) and Data Cleansing*: 
   - Perform EDA to identify patterns, inconsistencies, or outliers before loading the data into GCS.
   - Cleanse the data by:
     - Removing duplicates or irrelevant records.
     - Standardizing formats (e.g., dates, numeric values).
     - Addressing rogue or incomplete records.
   - Upload both raw and cleaned files to GCS.

3. *Data Upload*: 
   - Implement functionality within the Python program to upload the generated CSV files to Google Cloud Storage (GCS).

4. *Data Loading*: 
   - Utilize BigQuery to load cleansed CSV data from GCS, configuring BigQuery tables to accommodate the E-Commerce data structure for efficient querying.

5. *Data Analysis*: 
   - Perform analysis within BigQuery to answer key marketing questions:
     - Identify the top-selling product categories by country.
     - Analyze product popularity trends throughout the year by country.
     - Determine locations with the highest sales traffic.
     - Assess peak sales times by country.
     - Calculate the average order value across different product categories by country.
     - Analyze how payment methods impact sales volume and success rates by country.
     - Identify common reasons for payment failures and how they vary by country.

6. *Data Visualization*: 
   - Connect BigQuery to Looker Studio to create dynamic visualizations, providing actionable insights for the marketing team.

## Project Structure

- *requirements.txt*: Contains all the dependencies required for the project.
- *generator.py*: Generates synthetic e-commerce transaction data using the Faker module.
- *EDA.py*: Performs Exploratory Data Analysis (EDA) to detect patterns, trends, and anomalies in the generated data.
- *cleaning.py*: Cleans the data by handling missing values, rogue entries, and any data inconsistencies.
- *upload_to_gcs.py*: Uploads cleaned data files to Google Cloud Storage (GCS).
- *main.py*: Executes all modules in sequence to complete the data processing pipeline.
- *loading_bq.py*: uploading the data from bucket to big query and creating tables based on auto-detect schema for analysis.

## Data Analysis

Analyze the following marketing questions in BigQuery:
1. What is the top-selling category of items per country?
2. How does product popularity change throughout the year per country?
3. Which locations see the highest traffic of sales?
4. What times have the highest sales traffic per country?
5. What is the average order value across product categories per country?
6. How do payment methods impact sales and success rates per country?
7. What are the common reasons for payment failures, and how do they vary by country?

## Data Visualization
- Visualize the analysis results using Looker Studio, providing actionable insights for stakeholders.


## Google Cloud Configuration
- *Google Cloud Storage (GCS)*: Stores the raw and cleaned data.
- *BigQuery*: Stores the cleansed data and is used for performing data analysis.

## Visualization
- Connect BigQuery to *Looker Studio* to create dynamic visualizations.

## Data Schema
The project adheres to the following E-Commerce data schema:

| Field Name             | Description                                      |
|------------------------|--------------------------------------------------|
| order_id               | Order Id                                         |
| customer_id            | Customer Id                                      |
| customer_name          | Customer Name                                    |
| product_id             | Product Id                                       |
| product_name           | Product Name                                     |
| product_category       | Product Category                                 |
| payment_type           | Payment Type (Card, Internet Banking, UPI, Wallet)|
| qty                    | Quantity ordered                                 |
| price                  | Price of the product                             |
| datetime               | Date and time when the order was placed          |
| country                | Customer Country                                 |
| city                   | Customer City                                    |
| ecommerce_website_name | Site from where the order was placed             |
| payment_txn_id         | Payment Transaction Confirmation Id              |
| payment_txn_success    | Payment Success or Failure (Y=Success, N=Failed) |
| failure_reason         | Reason for payment failure                       |

## Future Improvements

- Add real-time data streaming and processing.
- Extend analysis to include machine learning predictions.
- Optimize DAG for faster execution and scalability.

## Definition of Done
The project is considered complete when:
- The Python program successfully generates a CSV file with 10,000 records, including rogue entries.
- The generated CSV data is uploaded to GCS and loaded into BigQuery without errors.
- Data analysis queries are executed in BigQuery, providing accurate results for all predefined marketing questions.
- Visualizations in Looker Studio effectively display the data analysis results.
