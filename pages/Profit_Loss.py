import pandas as pd
import streamlit as st
from datetime import datetime


# Read expenses CSV file
expenses_df = pd.read_csv('expenses.csv')

# Access each Total Expense of Day of the date respectively
def get_total_expense(date):
    # Filter expenses DataFrame based on the date and sum Expense Amount
    total_expense = expenses_df.loc[expenses_df['Date'] == date, "Expense Amount"].sum()
    return total_expense


# Read CSV files
order_book = pd.read_csv('./data/order_book.csv')
hs_data = pd.read_csv('./data/hs_data.csv')
ms_data = pd.read_csv('./data/ms_data.csv')
xp_data = pd.read_csv('./data/xp_data.csv')

# Merge the dataframes
merged_data = pd.merge(order_book, hs_data, on='Date')
merged_data = pd.merge(merged_data, ms_data, on='Date')
merged_data = pd.merge(merged_data, xp_data, on='Date')

# Calculate revenues
merged_data['HS Revenue'] = merged_data['HS Commission'] * merged_data['HS Actual Nozzle Sales']
merged_data['MS Revenue'] = merged_data['MS Commission'] * merged_data['MS Actual Nozzle Sales']
merged_data['XP Revenue'] = merged_data['XP Commission'] * merged_data['XP Actual Nozzle Sales']

# Calculate total expenses
merged_data['Total Expenses'] = merged_data['Date'].apply(get_total_expense)

# Calculate total revenue
merged_data['Total Revenue'] = merged_data['HS Revenue'] + merged_data['MS Revenue'] + merged_data['XP Revenue']

# Calculate day's profit
merged_data["Day's Profit"] = merged_data['Total Revenue'] - merged_data['Total Expenses']

# Display the table in Streamlit
st.write(merged_data)
