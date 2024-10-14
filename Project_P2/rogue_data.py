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

# Function to generate a single rogue record
def generate_rogue_record():
    category = random.choice(data['categories'])
    product_names = data['products'].get(category, ['InvalidProduct', None, ''])
    product_name = random.choice(product_names)
    
    payment_success = random.choice(data['payment_status'])
    failure_reason = random.choice(data['failure_reasons']) if payment_success == 'N' else ''
    
    # Handle rogue data characteristics
    return {
        'Order_id': fake.uuid4() if random.choice([True, False]) else '',  # Missing ID
        'Customer_id': fake.uuid4() if random.choice([True, False]) else None,
        'Customer_name': fake.name() if random.choice([True, False]) else '',
        'Product_id': fake.uuid4() if random.choice([True, False]) else 'InvalidID',
        'Product_name': product_name,
        'Product_category': category,
        'Payment_type': random.choice(data['payment_types']),
        'Quantity_ordered': random.randint(-5, 10),  # Negative quantity possible
        'Price': round(random.uniform(-100, 1000), 2),  # Negative price possible
        'Date_and_time_when_order_was_placed': fake.date_time_this_decade() if random.choice([True, False]) else 'InvalidDate',
        'Customer_country': random.choice(data['countries']),
        'Customer_city': fake.city() if random.choice([True, False]) else '',
        'Site_from_where_order_was_placed': random.choice(data['sites']),
        'Payment_transaction_confirmation_id': fake.uuid4() if random.choice([True, False]) else '',
        'Payment_success_or_failure': payment_success,
        'Reason_for_payment_failure': failure_reason
    }

# Function to generate multiple rogue records
def generate_rogue_records(num_records):
    records = [generate_rogue_record() for _ in range(num_records)]
    return records

# Function to save rogue records to CSV
def save_records_to_csv(filename, records):
    if records:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=records[0].keys())
            writer.writeheader()
            writer.writerows(records)
    else:
        print("No records to save.")

