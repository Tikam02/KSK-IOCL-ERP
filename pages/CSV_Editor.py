import streamlit as st
import pandas as pd
import os

def add_initial_value_to_csv(csv_file_path, initial_value):
    # Read CSV file
    df = pd.read_csv(csv_file_path)

    # Add initial value to the "HS Opening Stock" column
    df['HS Opening Stock'] = initial_value

    return df

def main():
    st.title("CSV Initial Value Editor")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read uploaded CSV file
        df = pd.read_csv(uploaded_file)

        # Display original DataFrame
        st.subheader("Original Data:")
        st.write(df)

        # Initial value input
        initial_value = st.number_input("Enter the initial value for 'HS Opening Stock'", value=0.0)

        # Button to add initial value
        if st.button("Add Initial Value"):
            # Add initial value to the CSV
            df['HS Opening Stock'] = initial_value

            # Display modified DataFrame
            st.subheader("Modified Data:")
            st.write(df)

            # Save modified CSV file
            csv_save_path = "./data/hs_data.csv"
            df.to_csv(csv_save_path, index=False)
            st.success(f"Modified data saved to {csv_save_path}")

if __name__ == "__main__":
    main()
