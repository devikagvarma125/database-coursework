import pyodbc
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

# Database connection credentials
server = 'tcp:mcruebs04.isad.isadroot.ex.ac.uk' 
database = 'BEMM459_GroupJ'
username = 'GroupJ' 
password = 'OvuI502+Xp'

# Establish connection with the database
connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';TrustServerCertificate=yes;Encrypt=no;')
cursor = connection.cursor()

# Read the customer_dataset.csv file and insert its contents into the customer table created in the database
data = pd.read_csv("customers_dataset.csv")
df = pd.DataFrame(data)

for row in df.itertuples(index=False):
    cursor.execute("INSERT INTO dbo.customer_details (customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state) values (?,?,?,?,?)", row.customer_id, row.customer_unique_id, row.customer_zip_code_prefix, row.customer_city, row.customer_state)
connection.commit()

# Read the sellers_dataset.csv file and insert its contents into the seller table created in the database
data = pd.read_csv("sellers_dataset.csv")
df = pd.DataFrame(data)

for row in df.itertuples(index=False):
    cursor.execute("INSERT INTO dbo.seller_details (seller_id, seller_zip_code_prefix, seller_city, seller_state) values (?,?,?,?)", row.seller_id, row.seller_zip_code_prefix, row.seller_city, row.seller_state)
connection.commit()

# Read the products_dataset.csv file and insert its contents into the products table created in the database
data = pd.read_csv("products_dataset.csv")
df = pd.DataFrame(data)

for row in df.itertuples(index=False):
    cursor.execute("INSERT INTO dbo.products_details (product_id, seller_id, product_category_name, quantity_remaining) values (?,?,?,?)", row.product_id, row.seller_id, row.product_category_name, row.quantity_remaining)
connection.commit()

# Read the orders_dataset.csv file and insert its contents into the orders table created in the database
data = pd.read_csv("orders_dataset.csv")
df = pd.DataFrame(data)

for row in df.itertuples(index=False):
    cursor.execute("INSERT INTO dbo.orders_details (order_id, customer_id, seller_id, order_status, order_purchase_date, order_delivered_carrier_date, order_delivered_customer_date) values (?,?,?,?,?,?,?)", row.order_id, row.customer_id, row.seller_id, row.order_status, row.order_purchase_date, row.order_delivered_carrier_date, row.order_delivered_customer_date)
connection.commit()

# Read the order_payments_dataset.csv file and insert its contents into the order_payments table created in the database
data = pd.read_csv("order_payments_dataset.csv")
df = pd.DataFrame(data)

for row in df.itertuples(index=False):
    cursor.execute("INSERT INTO dbo.order_payments_details (order_id, payment_sequential, payment_type, payment_installments, payment_value) values (?,?,?,?,?)", row.order_id, row.payment_sequential, row.payment_type, row.payment_installments, row.payment_value)
connection.commit()

# Read the order_items_payments_dataset.csv file and insert its contents into the order_items table created in the database
data = pd.read_csv("order_items_dataset.csv")
df = pd.DataFrame(data)

for row in df.itertuples(index=False):
    cursor.execute("INSERT INTO dbo.order_items_details (order_id, order_item_id, product_id, shipping_limit_date, price, freight_value) values (?,?,?,?,?,?)", row.order_id, row.order_item_id, row.product_id, row.shipping_limit_date, row.price, row.freight_value)
connection.commit()

cursor.close()
connection.close()