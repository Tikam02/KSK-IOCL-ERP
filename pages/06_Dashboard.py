import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the expense data
expense_df = pd.read_csv("./data/variable_expenses.csv")
fixed_expense_df = pd.read_csv("./data/fixed_expenses.csv")

# Combine the dataframes
combined_df = pd.concat([expense_df, fixed_expense_df], ignore_index=True)

# Group by date and calculate total daily expense
total_daily_expense = combined_df.groupby('Date')['Amount'].sum().reset_index()

# Plot the total daily expense
st.title("Expense Analysis")
st.subheader("Total Daily Expense")
plt.figure(figsize=(10, 6))
plt.bar(total_daily_expense['Date'], total_daily_expense['Amount'])
plt.xlabel('Date')
plt.ylabel('Total Expense')
plt.xticks(rotation=45)
st.pyplot()

# Show the combined dataframe
st.subheader("Combined Expense Data")
st.write(combined_df)
