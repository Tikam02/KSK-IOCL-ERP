# import streamlit as st
# import pandas as pd
# import os

# # Load data from CSV files
# order_book = pd.read_csv('./data/order_book.csv')
# hs_data = pd.read_csv('./data/hs_data.csv')
# fe_data = pd.read_csv('./data/fixed_expenses.csv')
# ve_data = pd.read_csv('./data/variable_expenses.csv')

# # Merge the two dataframes on the 'Date' column and keep only the last occurrence of each date
# merged_data = pd.merge(order_book, hs_data, on='Date').drop_duplicates(subset=['Date'])
# fixed_expenses = fe_data.groupby('Date').last().reset_index()
# variable_expenses = ve_data.groupby('Date').last().reset_index()

# # Calculate revenue for each row
# merged_data['Revenue'] = merged_data['Actual Nozzle Sales'] * merged_data['HS Commission']

# # Calculate total expenses
# total_fixed_expenses = fixed_expenses["Total Daily Expense"].sum()
# total_variable_expenses = variable_expenses["Total Daily Expense"].sum()

# # Calculate Profits
# total_revenue = merged_data['Revenue'].sum()
# total_expense = total_fixed_expenses + total_variable_expenses
# day_profit = total_revenue - total_expense

# # Display the revenue in a Streamlit app
# st.title('Revenue Calculation App')

# # Display the merged data
# st.subheader('Merged Data')
# st.dataframe(merged_data)

# # Display the revenue column
# st.subheader('Revenue Column')
# st.write(merged_data[['Date', 'Actual Nozzle Sales', 'HS Commission', 'Revenue']])

# # Display the total revenue
# st.subheader('Total Revenue')
# st.write(f'Total Revenue: ${total_revenue:.2f}')

# # Display the total expenses
# st.subheader('Total Expenses')
# st.write(f'Total Fixed Expenses: ${total_fixed_expenses:.2f}')
# st.write(f'Total Variable Expenses: ${total_variable_expenses:.2f}')

# # Display the day's profit
# st.subheader("Day's Profit")
# st.write(f"Day's Profit: ${day_profit:.2f}")

# # Save data to CSV files
# output_folder = "./data/khata_book/"
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# merged_data.to_csv(os.path.join(output_folder, "khata_book.csv"), index=False)
# st.success(f"Data saved to {os.path.join(output_folder, 'khata_book.csv')}")

import streamlit as st
import pandas as pd
import os

# Load data from CSV files
order_book = pd.read_csv('./data/order_book.csv')
hs_data = pd.read_csv('./data/hs_data.csv')
fe_data = pd.read_csv('./data/fixed_expenses.csv')
ve_data = pd.read_csv('./data/variable_expenses.csv')

# Merge the two dataframes on the 'Date' column and keep only the last occurrence of each date
merged_data = pd.merge(order_book, hs_data, on='Date').drop_duplicates(subset=['Date'])
fixed_expenses = fe_data.groupby('Date').last().reset_index()
variable_expenses = ve_data.groupby('Date').last().reset_index()

# Calculate revenue for each row
merged_data['HS Revenue'] = merged_data['HS Actual Nozzle Sales'] * merged_data['HS Commission']
merged_data['MS Revenue'] = merged_data['MS Actual Nozzle Sales'] * merged_data['MS Commission']
merged_data['XP Revenue'] = merged_data['XP Actual Nozzle Sales'] * merged_data['XP Commission']


# Calculate total expenses
total_fixed_expenses = fixed_expenses["Total Daily Expense"].sum()
total_variable_expenses = variable_expenses["Total Daily Expense"].sum()

# Calculate Profits
total_revenue = merged_data['HS Revenue'] + merged_data['HS Revenue'] + merged_data['HS Revenue']
total_expense = total_fixed_expenses + total_variable_expenses
day_profit = total_revenue - total_expense

# Add additional columns to the merged data
merged_data["Total Fixed Expenses"] = total_fixed_expenses
merged_data["Total Variable Expenses"] = total_variable_expenses
merged_data["Day's Profit"] = day_profit

# Display the revenue and additional columns in a Streamlit app
st.title('Revenue Calculation App')

# Display the merged data with additional columns
st.subheader('Merged Data')
st.dataframe(merged_data)

# Display the total revenue
st.subheader('Total Revenue')
st.write(f'Total Revenue: ${total_revenue:.2f}')


# HS Comission = 
# MS Comission = 
# XP Comission = 

# HS Actual Nozzle Sales = 
# MS Actal Nozzle Sales = 
# XP Actal Nozzle Sales = 


# HS Revenue = HS Comission * HS Actual Nozzle Sales
# MS Revenue = MS Comission * MS Actual Nozzle Sales
# XP Revenue = XP Comission * XP Actual Nozzle Sales
# Total Expenses = fixed expenses + variable expenses 
# Total Revenue = HS Revenue + MS Revenue + XP Revenue 
# Day's Profit = Total Revenue - Total Expenses



# Display the total expenses
st.subheader('Total Expenses')
st.write(f'Total Fixed Expenses: ${total_fixed_expenses:.2f}')
st.write(f'Total Variable Expenses: ${total_variable_expenses:.2f}')

# Display the day's profit
st.subheader("Day's Profit")
st.write(f"Day's Profit: ${day_profit:.2f}")

# Save data to CSV files
output_folder = "./data/khata_book/"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Save the merged data to CSV
merged_data.to_csv(os.path.join(output_folder, "khata_book.csv"), index=False)
st.success(f"Data saved to {os.path.join(output_folder, 'khata_book.csv')}")
