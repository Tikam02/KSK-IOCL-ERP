import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Display input forms and editable fields
st.title("Fuel Order Management")


# Input forms for date and products in litres
date = st.date_input("Date", datetime.now(), key="date")
hs_products_litres = st.number_input("HS Products in litres", min_value=0.0, value=0.0)
ms_products_litres = st.number_input("MS Products in litres", min_value=0.0, value=0.0)
xp_products_litres = st.number_input("XP Products in litres", min_value=0.0, value=0.0)


col1, col2 = st.columns(2)

# Purchasing cost
with col1:
    st.subheader("Purchasing cost")
    hs_purchasing_cost = st.number_input("HS Cost in Rupees", min_value=0.0, value=0.0)
    ms_purchasing_cost = st.number_input("MS Cost in Rupees", min_value=0.0, value=0.0)
    xp_purchasing_cost = st.number_input("XP Cost in Rupees", min_value=0.0, value=0.0)

# Editable fields
with col2:
    st.subheader("Price at  RO")
    hs_ro_price = st.number_input("HS RO Unit Price", min_value=0.0, value=97.39, format="%.2f")
    ms_ro_price = st.number_input("MS RO Unit Price", min_value=0.0, value=104.43, format="%.2f")
    xp_ro_price = st.number_input("XP RO Unit Price", min_value=0.0, value=107.78, format="%.2f")

# Initialize commission values in a dictionary
commission_values = {"hs": 0.0, "ms": 0.0, "xp": 0.0}

# Submit button to save data to CSV file
if st.button("Submit"):
    # Function to calculate and display values
    def calculate_values(commission_values, hs_purchasing_cost, ms_purchasing_cost, xp_purchasing_cost, hs_products_litres, ms_products_litres, xp_products_litres):
        # Calculate Unit Price at Depot
        hs_depot_price = hs_purchasing_cost / hs_products_litres
        ms_depot_price = ms_purchasing_cost / ms_products_litres
        xp_depot_price = xp_purchasing_cost / xp_products_litres

        # Use the current commission values
        hs_commission = hs_ro_price - hs_depot_price
        ms_commission = ms_ro_price - ms_depot_price
        xp_commission = xp_ro_price - xp_depot_price

        # Update the commission values in the dictionary
        commission_values["hs"] = hs_commission
        commission_values["ms"] = ms_commission
        commission_values["xp"] = xp_commission

        return hs_purchasing_cost, ms_purchasing_cost, xp_purchasing_cost, hs_depot_price, ms_depot_price, xp_depot_price, hs_commission, ms_commission, xp_commission

    # Calculate and display values
    if hs_products_litres > 0 and ms_products_litres > 0 and xp_products_litres > 0:
        hs_purchasing_cost, ms_purchasing_cost, xp_purchasing_cost, hs_depot_price, ms_depot_price, xp_depot_price, hs_commission, ms_commission, xp_commission = calculate_values(commission_values, hs_purchasing_cost, ms_purchasing_cost, xp_purchasing_cost, hs_products_litres, ms_products_litres, xp_products_litres)

        # Display calculated values in a table
        data = {
            "Date": [date],
            "HS Purchasing Cost": hs_purchasing_cost,
            "MS Purchasing Cost": ms_purchasing_cost, 
            "XP Purchasing Cost": xp_purchasing_cost,
            "HS Price at Depot": hs_depot_price, 
            "MS Price at Depot": ms_depot_price, 
            "XP Price at Depot": xp_depot_price,
            "HS Commission": hs_commission, 
            "MS Commission": ms_commission, 
            "XP Commission": xp_commission,
            "HS in Litres": hs_products_litres, 
            "MS in Litres": ms_products_litres,
            "XP in Litres": xp_products_litres
        }

        

        calculated_df = pd.DataFrame(data)
        st.table(calculated_df)

        # Save data to CSV file
        output_folder = "./data/"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        calculated_df.to_csv(os.path.join(output_folder, "order_book.csv"), mode='a', header=not os.path.exists(os.path.join(output_folder, "order_book.csv")), index=False)
