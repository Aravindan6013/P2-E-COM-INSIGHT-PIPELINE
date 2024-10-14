import random
import csv
from faker import Faker

# Initialize Faker instance
fake = Faker()

data = {
    'payment_types': ['Card', 'Internet Banking', 'UPI', 'Wallet'],
    'countries': ['USA', 'UK', 'Germany', 'India', 'Canada'],
    'categories': ['Stationery', 'Electronics', 'Clothing', 'Home & Kitchen', 'Sports'],
    'sites': ['www.amazon.com', 'www.ebay.com', 'www.flipkart.com', 'www.walmart.com', 'www.shopify.com'],
    'payment_status': ['Y', 'N'],
    'failure_reasons': ['Insufficient funds', 'Payment gateway error', 'Card expired', 'Invalid CVV', None],
    
    'products': {
        'Stationery': ["Pen", "Pencil", "Notebook", "Book", "Eraser", "Ruler", "Sharpener"],
        'Electronics': ["Smartphone", "Laptop", "Smartwatch", "Headphones", "Tablet", "Camera"],
        'Clothing': ["T-Shirt", "Jeans", "Jacket", "Shoes", "Socks", "Sweater"],
        'Home & Kitchen': ["Coffee Maker", "Blender", "Microwave", "Toaster", "Air Fryer", "Dishwasher"],
        'Sports': ["Basketball", "Football", "Tennis Racket", "Cricket Bat", "Badminton Racket", "Yoga Mat"]
    },
    
    'country_cities': {
    'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'UK': ['London', 'Manchester', 'Birmingham', 'Liverpool', 'Leeds'],
    'Germany': ['Berlin', 'Munich', 'Frankfurt', 'Hamburg', 'Cologne'],
    'India': ['Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Chennai'],
    'Canada': ['Toronto', 'Vancouver', 'Montreal', 'Calgary', 'Ottawa']
    }

}

# Function to generate a single valid record
def generate_valid_record():
    country = random.choice(data['countries'])
    city = random.choice(data['country_cities'][country])
    category = random.choice(list(data['products'].keys()))
    product_name = random.choice(data['products'][category])
    payment_success = random.choice(data['payment_status'])
    failure_reason = random.choice(data['failure_reasons']) if payment_success == 'N' else ''
    
    return {
        'Order_id': fake.uuid4(),
        'Customer_id': fake.uuid4(),
        'Customer_name': fake.name(),
        'Product_id': fake.uuid4(),
        'Product_name': product_name,
        'Product_category': category,
        'Payment_type': random.choice(data['payment_types']),
        'Quantity_ordered': random.randint(1, 5),
        'Price': round(random.uniform(10, 1000), 2),
        'Date_and_time_when_order_was_placed': fake.date_time_this_decade(),
        'Customer_country': country,
        'Customer_city': city,
        'Site_from_where_order_was_placed': random.choice(data['sites']),
        'Payment_transaction_confirmation_id': fake.uuid4(),
        'Payment_success_or_failure': payment_success,
        'Reason_for_payment_failure': failure_reason
    }

# Function to generate multiple records
def generate_records(num_records):
    records = [generate_valid_record() for _ in range(num_records)]
    return records

# Function to save records to CSV
def save_records_to_csv(filename, records):
    if records:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=records[0].keys())
            writer.writeheader()
            writer.writerows(records)
    else:
        print("No records to save.")


