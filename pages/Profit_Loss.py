# import streamlit as st
# import pandas as pd

# # Load data from CSV files
# order_book = pd.read_csv('./data/order_book.csv')
# hs_data = pd.read_csv('./data/hs_data.csv')

# # Merge the two dataframes on the 'Date' column
# merged_data = pd.merge(order_book, hs_data, on='Date')

# # Calculate revenue for each row
# merged_data['Revenue'] = merged_data['Actual Nozzle Sales'] * merged_data['HS Commission']

# # Display the revenue in a Streamlit app
# st.title('Revenue Calculation App')

# # Display the merged data
# st.subheader('Merged Data')
# st.dataframe(merged_data)

# # Display the revenue column
# st.subheader('Revenue Column')
# st.write(merged_data[['Date', 'Actual Nozzle Sales', 'HS Commission', 'Revenue']])

# # Display total revenue
# total_revenue = merged_data['Revenue'].sum()
# st.subheader('Total Revenue')
# st.write(f'Total Revenue: ${total_revenue:.2f}')

import streamlit as st
import pandas as pd

# Load data from CSV files
order_book = pd.read_csv('./data/order_book.csv')
hs_data = pd.read_csv('./data/hs_data.csv')

# Merge the two dataframes on the 'Date' column and keep only the first occurrence of each date
merged_data = pd.merge(order_book, hs_data, on='Date').drop_duplicates(subset=['Date'])

# Calculate revenue for each row
merged_data['Revenue'] = merged_data['Actual Nozzle Sales'] * merged_data['HS Commission']

# Display the revenue in a Streamlit app
st.title('Revenue Calculation App')

# Display the merged data
st.subheader('Merged Data')
st.dataframe(merged_data)

# Display the revenue column
st.subheader('Revenue Column')
st.write(merged_data[['Date', 'Actual Nozzle Sales', 'HS Commission', 'Revenue']])

# Display total revenue
total_revenue = merged_data['Revenue'].sum()
st.subheader('Total Revenue')
st.write(f'Total Revenue: ${total_revenue:.2f}')
