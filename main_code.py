import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import squarify as sq
import pymongo

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

# Display the names of all the tables created in the database
cursor.execute("SELECT table_name FROM information_schema.tables;")

name_of_tables = cursor.fetchall()

a = []
for i in name_of_tables:
    a.append(i[0])

names = ', '.join(map(str, a))

print('\nThe tables in SQL server are :', names)

# Display the contents of all the tables created in the database 
for table_name in a:
    print('\nTable name  : ', table_name, '\n')
    cursor.execute(f'EXEC SP_COLUMNS {table_name}')
    table_columns = cursor.fetchall()
    columns = []
    for item in table_columns:
        columns.append(item[3])
    cursor.execute(f"select * from {table_name}")
    table_data = cursor.fetchall()
    df = pd.DataFrame.from_records(table_data, columns = columns)
    print(df)

# Inserting a new record in the seller_details table
insert_query = "INSERT INTO seller_details(seller_id,seller_zip_code_prefix, seller_city, seller_state) VALUES (?,?, ?, ?)"
values = ('xca3071e3e9bb7d12640c9fbe2301309', '123456889', 'ABC','XYZ')
cursor.execute(insert_query, values)
connection.commit()

# Inserting a new record in the products_details table
insert_query = "INSERT INTO products_details(product_id,seller_id,product_category_name, quantity_remaining) VALUES (?,?, ?, ?)"
values = ('z249f9dc99c68bbd2e4301672e0f97c0','xca3071e3e9bb7d12640c9fbe2301309', 'Indoor plants', '112')
cursor.execute(insert_query, values)
connection.commit()

# Read records from seller_details and products_details table
select_query1 = "SELECT * FROM seller_details"
cursor.execute(select_query1)
print('\nTable name  : seller_details\n')
table_columns1 = cursor.fetchall()
df = pd.DataFrame.from_records(table_columns1, columns = ['seller_id','seller_zip_code_prefix', 'seller_city', 'seller_state'])
print(df.tail(5))

select_query2 = "SELECT * FROM products_details"
cursor.execute(select_query2)
print('\nTable name  : products_details\n')
table_columns2 = cursor.fetchall()
df = pd.DataFrame.from_records(table_columns2, columns = ['product_id', 'seller_id', 'product_category_name', 'quantity_remaining'])
print(df.tail(5))

# Update an existing record in the products_details table:
update_query = "UPDATE products_details SET product_category_name = 'Electronics' WHERE product_id = 'z249f9dc99c68bbd2e4301672e0f97c0'"
values = ('Electronics', 'Indoor plants')
cursor.execute(update_query)
connection.commit()
select_query = "SELECT * FROM products_details"
cursor.execute(select_query)
print('\nTable name  : products_details\n')
table_columns2 = cursor.fetchall()
df1 = pd.DataFrame.from_records(table_columns2, columns = ['product_id', 'seller_id', 'product_category_name', 'quantity_remaining'])
print(df1.tail(5))

# Deleting a record from product_details table
delete_query1 = "DELETE FROM products_details WHERE product_id = 'z249f9dc99c68bbd2e4301672e0f97c0'"
delete_query2 = "DELETE FROM seller_details WHERE seller_id = 'xca3071e3e9bb7d12640c9fbe2301309'"
cursor.execute(delete_query1)
cursor.execute(delete_query2)
connection.commit()

select_query1 = "SELECT * FROM seller_details"
cursor.execute(select_query1)
print('\nTable name  : seller_details\n')
table_columns1 = cursor.fetchall()
df1 = pd.DataFrame.from_records(table_columns1, columns = ['seller_id','seller_zip_code_prefix', 'seller_city', 'seller_state'])
print(df1.tail(5))

select_query2 = "SELECT * FROM products_details"
cursor.execute(select_query2)
print('\nTable name  : products_details\n')
table_columns2 = cursor.fetchall()
df2 = pd.DataFrame.from_records(table_columns2, columns = ['product_id', 'seller_id', 'product_category_name', 'quantity_remaining'])
print(df2.tail(5))

# Merge orders and order_items_details tables
sql_query1 = "SELECT * FROM order_items_details"
sql_query2 = "SELECT * FROM products_details"
df1 = pd.read_sql(sql_query1, connection)    
df2 = pd.read_sql(sql_query2, connection)

merged_data = pd.merge(df1, df2, on = 'product_id')

# Calculate total sales by product category
sales_by_category = merged_data.groupby('product_category_name').agg(total_sales = ('price', 'sum')).reset_index()

# Sort by total sales and take top 10 categories
top_categories = sales_by_category.sort_values('total_sales', ascending = False).head(10)

# Create a visualisation of the preferred product type based on sales
fig = plt.figure(figsize = (8, 6))
sq.plot(sizes = top_categories['total_sales'], label = top_categories['product_category_name'], color = ['red','green','blue', 'grey', 'white','pink','brown','yellow','orange', 'purple'], alpha = .8 )
plt.title("Most Preferred Product Category Based on Sales")
plt.axis('off')
plt.show()

# Visualisation to show cities with most number of customers
sql_query_city = "SELECT * FROM customer_details"
customers1 = pd.read_sql(sql_query_city, connection)

# Count the number of customers in each state
state_counts = customers1["customer_city"].value_counts()
rslt_df = state_counts.loc[state_counts.values != 1]

# Create a bar chart of the state counts
plt.bar(rslt_df.index, rslt_df.values, color = 'orange')
plt.xticks(rotation=90)
plt.title("Number of Customers in Each City")
plt.xlabel("State")
plt.ylabel("Number of Customers")
plt.show()

# Visualisation on number of orders by date
sql_query3 = "SELECT * FROM orders_details"
orders_df = pd.read_sql(sql_query3, connection)

# Average number of orders by date
orders_by_date = orders_df.groupby(['order_purchase_date']).size().reset_index(name='count')

# Create a bar chart of orders by date
plt.bar(orders_by_date['order_purchase_date'], orders_by_date['count'], color = 'red')
plt.xlabel('Date')
plt.ylabel('Number of Orders')
plt.title('Orders by Date')
plt.show()

# MongoDB
# Connecting to cloud database for olist stores
mongoClient = pymongo.MongoClient('mongodb+srv://av429:wEUo9lGpOfH6EKUA@cluster0.itvtyze.mongodb.net/test')

# Displaying databasenames
names1 = ', '.join(map(str,mongoClient.list_database_names()))
print("\nThese are the databases: "+ names1)

myDB = mongoClient["Olist_database"]
print(myDB["Product_description"])

# Displaying collectionnames
productdescription=myDB['Product_description']
reviews=myDB['Reviews']
names2 = ', '.join(map(str, myDB.list_collection_names()))
print("These are the collections: "+names2)

# Creating a new entry using a random product_id under the product_category "cool stuff"
newentry={
 "product_id": "xyzzc90e84b1bf2e157637d63fe09a68",
   "product_category_name": "cool_stuff",
   "Product Description": "A miscellaneous category for unique and quirky items",
   "product_photos_qty": 2,
   "product_weight_g": 90,
  "product_length_cm": 10,
   "product_height_cm": 19,
   "product_width_cm": 9
 }
newentry2=productdescription.insert_one(newentry)
query1={"product_category_name":{'$regex':"cool_stuff"}}
for x in productdescription.find(query1):
    print(x)
    print("One document is added to the Cool stuff category")

# Updating the new entry's photos quantity in the Product_description collection
productdescription.update_one({"product_id":"xyzzc90e84b1bf2e157637d63fe09a68"},{"$set":{ "product_photos_qty": 3}})
for x in productdescription.find({"product_id":"xyzzc90e84b1bf2e157637d63fe09a68"}):
    print(x)
print("Photos quantity has been updated")

# Deleting the new entry from the "cool stuff" category
query3={"product_id": { "$regex": "xyzzc90e84b1bf2e157637d63fe09a68"}}
value=productdescription.delete_many(query3)
print(value.deleted_count,"documents deleted")
query4={"product_category_name":{'$regex':"cool_stuff"}}
for x in productdescription.find(query4):
   print(x)

# SQL and NoSQL linking

# We are using product_id 16ba44d9231d19fc57e0a4188d0ce1cf as example
productID = input("\nEnter the product id : ")

# Getting order_id for given product_id from order_items_details table
query = "select order_id from order_items_details where product_id = '{}'".format(productID)
cursor.execute(query)
rows = cursor.fetchone()
print("\nThe order id for the entered product id : {}".format(rows[0]))

# Getting review_comment_message for the given order_id from reviews collection
result = reviews.find_one({'order_id': rows[0]})
print("The review for the entered product id : {}\n".format(result['review_comment_message']))

cursor.close()
connection.close()