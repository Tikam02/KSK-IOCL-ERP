import streamlit as st
import pandas as pd

# Load the product data from a CSV file
product_data = pd.read_csv('product_data.csv')

# Function to get product price
def get_product_price(product_name):
    product_info = product_data[product_data['Product Name'] == product_name]
    if not product_info.empty:
        return product_info['Wholesale Price'].iloc[0], product_info['Retail Price'].iloc[0]
    else:
        return None, None

# Create a dictionary to store sales data
sales_data = {}

# Streamlit app
st.title("Product Sales")

# Inputs
date = st.date_input("Date")
product_name = st.selectbox("Product Name", product_data['Product Name'])
seller_name = st.text_input("Seller Name")

# Get product price based on the selected product
wholesale_price, retail_price = get_product_price(product_name)

# Display price if available
if wholesale_price is not None and retail_price is not None:
    st.write(f"Wholesale Price: {wholesale_price}")
    st.write(f"Retail Price: {retail_price}")

# Submit button
if st.button("Submit"):
    # Store sales data in the dictionary
    sale_date = date.strftime("%Y-%m-%d")
    if sale_date in sales_data:
        sales_data[sale_date].append({
            "Product Name": product_name,
            "Wholesale Price": wholesale_price,
            "Retail Price": retail_price,
            "Seller Name": seller_name
        })
    else:
        sales_data[sale_date] = [{
            "Product Name": product_name,
            "Wholesale Price": wholesale_price,
            "Retail Price": retail_price,
            "Seller Name": seller_name
        }]

    # Calculate total sales for the day
    sales_for_day = sales_data[sale_date]
    total_sales = sum([item['Retail Price'] for item in sales_for_day])
    st.write(f"Total Sales for {sale_date}: {total_sales}")

    # Display sales data in a table
    sales_table = pd.DataFrame(sales_for_day)
    st.write("Sales Data:")
    st.table(sales_table)