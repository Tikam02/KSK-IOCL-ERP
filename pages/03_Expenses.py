import streamlit as st
import pandas as pd

# Function to handle adding expenses
def add_expense(date, expense_for, expense_by, expense_amount):
    new_expense = {'Date': date,
                   'Expense For': expense_for,
                   'Expense By': expense_by,
                   'Expense Amount': expense_amount}
    # Append new expense to existing CSV file without removing old data
    with open('expenses.csv', 'a') as f:
        pd.DataFrame([new_expense]).to_csv(f, header=f.tell()==0, index=False)

# Function to calculate total expenses for each day
def calculate_total_expenses():
    # Read expenses from CSV file
    expenses_df = pd.read_csv('expenses.csv')
    # Group by date and sum up expenses for each day
    total_expenses = expenses_df.groupby('Date')['Expense Amount'].sum()
    return total_expenses

# Main function
def main():
    st.title("Expense Tracker")

    # Create input forms
    with st.form("expense_form"):
        st.header("Enter Expense Details")

        date = st.date_input("Date")
        expense_for = st.text_input("Expense For")
        expense_by = st.text_input("Expense By")
        expense_amount = st.number_input("Expense Amount", step=0.01)

        submit_button = st.form_submit_button(label="Add Expense")

    # Handle submitted form
    if submit_button:
        add_expense(date, expense_for, expense_by, expense_amount)
        st.write("Expense added successfully.")

    # Calculate and display total expenses for each day
    total_expenses = calculate_total_expenses()
    st.subheader("Total Expenses for Each Day")
    st.write(total_expenses)

if __name__ == "__main__":
    main()
