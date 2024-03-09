import streamlit as st
import pandas as pd
from datetime import datetime

def main():
    st.title("Expenses Page")

    # Variable Expenses Section
    st.header("Variable Expenses")
    variable_expenses = create_expense_section("Variable", ["Date", "Expense Name", "Amount"])

    # Calculate Total Day's Expense for Variable Expenses
    variable_expenses["Total Daily Expense"] = variable_expenses.groupby("Date")["Amount"].transform(lambda x: pd.to_numeric(x, errors='coerce').fillna(0).sum())

    # Display Variable Expenses Table
    st.subheader("Variable Expenses Table")
    st.table(variable_expenses)

    # Fixed Expenses Section
    st.header("Fixed Expenses")

    # Dropdown for constants
    constants = ["Salary", "Electricity Bill", "Loan Interests", "Tanker Driver Allowance"]
    selected_constant = st.selectbox("Select Constant Expense:", constants)

    # Create Fixed Expenses
    fixed_expenses = create_expense_section("Fixed", ["Date", selected_constant, "Amount"])

    # Calculate Total Day's Expense for Fixed Expenses
    fixed_expenses["Total Daily Expense"] = fixed_expenses.groupby("Date")["Amount"].transform(lambda x: pd.to_numeric(x, errors='coerce').fillna(0).sum())


    # Display Fixed Expenses Table
    st.subheader("Fixed Expenses Table")
    st.table(fixed_expenses)

    # Save button
    if st.button("Save Expenses"):
        save_data(variable_expenses, "variable_expenses.csv")
        save_data(fixed_expenses, "fixed_expenses.csv")

def create_expense_section(section_name, default_fields):
    st.subheader(f"{section_name} Expenses")

    # Create a dynamic form to add expenses
    num_expenses = st.number_input(f"Number of {section_name} Expenses", min_value=1, value=1)
    expense_data = []

    for i in range(num_expenses):
        st.write(f"Expense {i + 1}")
        expense = {}
        for field in default_fields:
            if field == "Date":
                expense[field] = st.date_input(f"**{field}**", datetime.now(), key=f"{section_name}_{i}_{field}")
            else:
                expense[field] = st.text_input(f"{field}:", key=f"{section_name}_{i}_{field}")

        expense_data.append(expense)

    # Create a DataFrame from the entered data
    df = pd.DataFrame(expense_data)

    return df

def save_data(data, filename):
    # Save data to CSV file
    save_path = f"./data/{filename}"
    data.to_csv(save_path, index=False)
    st.success(f"{filename} saved to {save_path}")

if __name__ == "__main__":
    main()
