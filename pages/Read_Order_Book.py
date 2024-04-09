import streamlit as st
import pandas as pd

# Streamlit app title
st.title('Order Book Data Editor')

# File path
file_path = "./data/order_book.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Fill NaN values with 0
df.fillna(0, inplace=True)

# Display data in a data editor
edited_df = st.dataframe(df)

# If you want to allow editing and update the DataFrame
edited_df = st.data_editor(df)

# Retrieve specific information from the edited data
favorite_command = edited_df.loc[edited_df["HS in Litres"].idxmax()]["Date"]
st.write("Favorite command based on HS Receipt:", favorite_command)

# Save the updated data to the original order_book.csv file
if st.button("Save Changes"):
    edited_df.to_csv(file_path, index=False)
    st.success("Changes saved successfully.")
