import streamlit as st
import pandas as pd

# Read data from CSV files
data_df = pd.read_csv("./data.csv")

# Read Transport Data
tdata_df = pd.read_csv("./data/transport_ops_data.csv")

# Sort the DataFrame by the 'Date' column to ensure proper calculation of next day's values
data_df.sort_values(by='Date', inplace=True)

# Clean the data by removing commas and converting to numeric format if necessary
def clean_numeric_data(series):
    if series.dtype == 'O':  # Check if the column is of object type (likely contains strings)
        return pd.to_numeric(series.str.replace(',', ''), errors='coerce')
    else:
        return series

data_df['HS Nozzle 1'] = clean_numeric_data(data_df['HS Nozzle 1'])
data_df['HS Nozzle 2'] = clean_numeric_data(data_df['HS Nozzle 2'])
data_df['HS Nozzle 3'] = clean_numeric_data(data_df['HS Nozzle 3'])
data_df['HS Stock Volume'] = clean_numeric_data(data_df['HS Stock Volume'])
data_df['Physical Stock'] = clean_numeric_data(data_df['HS Stock Volume'])
data_df['Opening Stock'] = data_df['Physical Stock'].shift(1)
data_df["Receipt"] = clean_numeric_data(tdata_df['HS Order Quantity'])


total = (data_df['Physical Stock'].shift(1)+ clean_numeric_data(tdata_df['HS Order Quantity']))
print("hello",total)



# data_df['Opening Stock'] = clean_numeric_data(data_df['Opening Stock'])
# data_df['Closing Stock'] = clean_numeric_data(data_df['Opening Stock'])
# data_df['Loss_Gain Stock'] = clean_numeric_data(data_df['Loss_Gain Stock'])
# data_df['Cumm LnG Stock'] = clean_numeric_data(data_df['Cumm LnG Stock'])
# data_df['Testing'] = clean_numeric_data(data_df['Cumm LnG Stock'])
# data_df['Actual Nozzle Sales'] = clean_numeric_data(data_df['Cumm LnG Stock'])


################################# M S #################################################
# Calculate the difference between consecutive days for each nozzle
hs_nozzle1_diff = data_df['HS Nozzle 1'].diff().shift(-1)
hs_nozzle2_diff = data_df['HS Nozzle 2'].diff().shift(-1)
hs_nozzle3_diff = data_df['HS Nozzle 3'].diff().shift(-1)
# MS Nozzle Sales 
data_df['MS Nozzle 1'] = clean_numeric_data(data_df['MS Nozzle 1'])
data_df['MS Nozzle 2'] = clean_numeric_data(data_df['MS Nozzle 2'])

# Calculate the difference between consecutive days for each nozzle
ms_nozzle1_diff = data_df['MS Nozzle 1'].diff().shift(-1)
ms_nozzle2_diff = data_df['MS Nozzle 2'].diff().shift(-1)


####################################################################################

# XP Nozzle Sales 
data_df['XP Nozzle 1'] = clean_numeric_data(data_df['XP Nozzle 1'])
# Calculate the difference between consecutive days for each nozzle
xp_nozzle1_diff = data_df['XP Nozzle 1'].diff().shift(-1)

# HS Calculate the total nozzle sales for each day
hs_total_nozzle_sales = (hs_nozzle1_diff + hs_nozzle2_diff + hs_nozzle3_diff).fillna(0)
# MS Calculate the total nozzle sales for each day
ms_total_nozzle_sales = (ms_nozzle1_diff + ms_nozzle2_diff).fillna(0)
# XP Calculate the total nozzle sales for each day
xp_total_nozzle_sales = (ms_nozzle1_diff + xp_nozzle1_diff).fillna(0)

# Add the 'HS_Total Nozzle sales' column to the DataFrame
data_df['HS_Total Nozzle sales'] = hs_total_nozzle_sales
data_df['MS_Total Nozzle sales'] = ms_total_nozzle_sales
data_df['XP_Total Nozzle sales'] = xp_total_nozzle_sales


# Create separate DataFrames for HS, MS, and XP
hs_cal = pd.DataFrame({
    "Date": data_df["Date"],
    "DIP": data_df["HS DIP"],
    "HS Nozzle 1": data_df["HS Nozzle 1"],
    "HS Nozzle 2": data_df["HS Nozzle 2"],
    "HS Nozzle 3": data_df["HS Nozzle 3"],
    "HS_Total Nozzle sales": hs_total_nozzle_sales,
    "HS Stock Volme": data_df['HS Stock Volume'],
    "Physical Volume": data_df['HS Stock Volume'],
    "Opening Stock": data_df['Physical Stock'].shift(1),
    "Receipt": tdata_df['HS Order Quantity'],
})

ms_cal = pd.DataFrame({
    "Date": data_df["Date"],
    "DIP": data_df["MS DIP"],
    "MS Nozzle 1": data_df["MS Nozzle 1"],
    "MS Nozzle 2": data_df["MS Nozzle 2"],
    "MS_Total Nozzle sales": ms_total_nozzle_sales
})


xp_cal = pd.DataFrame({
    "Date": data_df["Date"],
    "DIP": data_df["XP DIP"],
    "XP Nozzle 1": data_df["XP Nozzle 1"],
    "XP_Total Nozzle sales": xp_total_nozzle_sales
})

# Display the tables in Streamlit
st.subheader("HS Nozzle Data")
st.table(hs_cal)

st.subheader("MS Nozzle Data")
st.table(ms_cal)

st.subheader("XP Nozzle Data")
st.table(xp_cal)
