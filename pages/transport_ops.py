import streamlit as st
import pandas as pd

def main():
    local_image_path = "./assets/vehicle.png"
    st.image(local_image_path, use_column_width=True, width=200)
    st.markdown("<h1 style='text-align: center; orange: red;'>Transport Operations</h1>", unsafe_allow_html=True)

    # Create an input container
    with st.container():
        # Date input
        date = st.date_input("Date", pd.to_datetime("today"))

        st.header("Product Order Quantity Litres")

        # HS, MS, and XP input fields
        hs_quantity = st.number_input("HS", min_value=0.0, step=0.01, format="%.2f")
        ms_quantity = st.number_input("MS", min_value=0.0, step=0.01, format="%.2f")
        xp_quantity = st.number_input("XP", min_value=0.0, step=0.01, format="%.2f")

        st.header("Purchasing Cost")

        # Constants (editable)
        ms_price = st.number_input("MS Price (per litre)", value=104.43, min_value=0.0, step=0.01, format="%.2f")
        hs_price = st.number_input("HS Price (per litre)", value=97.39, min_value=0.0, step=0.01, format="%.2f")
        xp_price = st.number_input("XP Price (per litre)", value=107.78, min_value=0.0, step=0.01, format="%.2f")

        # Calculate total cost
        hs_cost = hs_quantity * hs_price
        ms_cost = ms_quantity * ms_price
        xp_cost = xp_quantity * xp_price

        # Display the calculated total cost
        st.subheader("Total Cost:")
        st.write(f"HS Cost: {hs_cost:.2f}")
        st.write(f"MS Cost: {ms_cost:.2f}")
        st.write(f"XP Cost: {xp_cost:.2f}")

        # Constants for display
        constants = {
            "MS Price": ms_price,
            "HS Price": hs_price,
            "XP Price": xp_price
        }

        # Display the constants
        st.subheader("Constants:")
        st.write(constants)

        # Create a DataFrame with the entered data
        data = {
            "Date": [date],
            "HS Order Quantity": [hs_quantity],
            "MS Order Quantity": [ms_quantity],
            "XP Order Quantity": [xp_quantity],
            "HS Purchasing Cost": [hs_cost],
            "MS Purchasing Cost": [ms_cost],
            "XP Purchasing Cost": [xp_cost]
        }

        df = pd.DataFrame(data)

        # Display the entered data in a table
        st.subheader("Entered Data:")
        st.table(df)

        # Submit button to save data
        if st.button("Submit"):
            save_to_csv(df)

def save_to_csv(df):
    # Specify the folder path
    folder_path = "./data/"

    # Load existing data from CSV
    try:
        existing_df = pd.read_csv(folder_path + "transport_data.csv")
    except FileNotFoundError:
        # Create a new DataFrame if the file doesn't exist
        existing_df = pd.DataFrame(columns=["Date", "HS Order Quantity", "MS Order Quantity", "XP Order Quantity",
                                            "HS Purchasing Cost", "MS Purchasing Cost", "XP Purchasing Cost"])

    # Append the new data to the existing DataFrame
    combined_df = pd.concat([existing_df, df], ignore_index=True)

    # Save the combined DataFrame to the CSV file
    combined_df.to_csv(folder_path + "transport_ops_data.csv", index=False)

if __name__ == "__main__":
    main()
