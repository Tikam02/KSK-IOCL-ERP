import streamlit as st
import pandas as pd

def show_data():
    st.title("Show All Data")

    try:
        # Load all data from CSV
        df = pd.read_csv("data.csv")

        # Set a custom width for the table
        st.write(df, width=1000)  # Adjust the width as needed

    except FileNotFoundError:
        st.error("Data file 'data.csv' not found. No data available.")

    except pd.errors.EmptyDataError:
        st.warning("Data file 'data.csv' is empty. No data available.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    show_data()
