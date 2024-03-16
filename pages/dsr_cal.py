import streamlit as st
import pandas as pd
import os


# Read data from CSV files
data_df = pd.read_csv("./data.csv")

# Read Transport Data
tdata_df = pd.read_csv("./data/order_book.csv")


# Read the CSV files
order_book_df = pd.read_csv("./data/order_book.csv")
data_df = pd.read_csv("./data.csv")

# Merge the data frames on the "Date" column
merged_df = pd.merge(data_df, order_book_df, on="Date", how="left")

# Fill missing values with 0
merged_df.fillna(0, inplace=True)

# Convert date column to datetime format
merged_df['Date'] = pd.to_datetime(merged_df['Date'])

# Display the merged dataframe in Streamlit
st.table(merged_df)

# Sort the DataFrame by the 'Date' column to ensure proper calculation of next day's values
data_df.sort_values(by='Date', inplace=True)

# Clean the data by removing commas and converting to numeric format if necessary
def clean_numeric_data(series):
    if series.dtype == 'O':  # Check if the column is of object type (likely contains strings)
        return pd.to_numeric(series.str.replace(',', ''), errors='coerce')
    else:
        return series
    


################################# H S #################################################
# Calculate the difference between consecutive days for each nozzle
hs_nozzle1_diff = data_df['HS Nozzle 1'].diff().shift(-1)
hs_nozzle2_diff = data_df['HS Nozzle 2'].diff().shift(-1)
hs_nozzle3_diff = data_df['HS Nozzle 3'].diff().shift(-1)



# HS Calculate the total nozzle sales for each day
hs_total_nozzle_sales = (hs_nozzle1_diff + hs_nozzle2_diff + hs_nozzle3_diff).fillna(0)
data_df['HS Nozzle 1'] = clean_numeric_data(data_df['HS Nozzle 1'])
data_df['HS Nozzle 2'] = clean_numeric_data(data_df['HS Nozzle 2'])
data_df['HS Nozzle 3'] = clean_numeric_data(data_df['HS Nozzle 3'])
hs_stock_volume = clean_numeric_data(data_df['HS Stock Volume'])
data_df['HS Physical Stock'] = clean_numeric_data(data_df['HS Stock Volume'])
data_df['HS Opening Stock'] = data_df['HS Physical Stock'].shift(1)

# # Fetching receipt data from 'tdata_df'
# hs_receipt_data = tdata_df.set_index('Date')['HS in Litres']
# # Ensure the index of receipt_data is unique
# hs_receipt_data = hs_receipt_data[~hs_receipt_data.index.duplicated(keep='first')]
# hs_receipt_data = hs_receipt_data.replace("<NA>", pd.NA).fillna(0)
# Fetching receipt data from 'tdata_df'
hs_receipt_data = tdata_df.set_index('Date')['HS in Litres']
# Ensure the index of receipt_data is unique
hs_receipt_data = hs_receipt_data[~hs_receipt_data.index.duplicated(keep='first')]
# Replace missing values with 0
hs_receipt_data = hs_receipt_data.fillna(0)



#HS Physical Stock
hs_physical_stock = data_df['HS Physical Stock']
print("Physical",hs_receipt_data)

hs_testing = 10

hs_total_stock = hs_physical_stock + hs_receipt_data 
hs_actual_nozzle_sales  = hs_total_nozzle_sales - hs_testing
hs_closing_stock = hs_actual_nozzle_sales - hs_total_stock
hs_loss_gain_stock = hs_stock_volume - hs_closing_stock


# data_df['Loss_Gain Stock'] = clean_numeric_data(data_df['Loss_Gain Stock'])
# data_df['Cumm LnG Stock'] = clean_numeric_data(data_df['Cumm LnG Stock'])

##-----------------------------------------MS--------------------------------------

# MS Nozzle Sales 
data_df['MS Nozzle 1'] = clean_numeric_data(data_df['MS Nozzle 1'])
data_df['MS Nozzle 2'] = clean_numeric_data(data_df['MS Nozzle 2'])

# Calculate the difference between consecutive days for each nozzle
ms_nozzle1_diff = data_df['MS Nozzle 1'].diff().shift(-1)
ms_nozzle2_diff = data_df['MS Nozzle 2'].diff().shift(-1)


# HS Calculate the total nozzle sales for each day
ms_total_nozzle_sales = (ms_nozzle1_diff + ms_nozzle2_diff).fillna(0)
data_df['MS Nozzle 1'] = clean_numeric_data(data_df['MS Nozzle 1'])
data_df['MS Nozzle 2'] = clean_numeric_data(data_df['MS Nozzle 2'])
data_df['MS Stock Volume'] = clean_numeric_data(data_df['MS Stock Volume'])
data_df['MS Physical Stock'] = clean_numeric_data(data_df['MS Stock Volume'])
data_df['MS Opening Stock'] = data_df['MS Physical Stock'].shift(1)

# Fetching receipt data from 'tdata_df'
ms_receipt_data = tdata_df.set_index('Date')['MS in Litres']

# MS Stock Volume
ms_stock_volume = data_df['MS Stock Volume']

# Ensure the index of receipt_data is unique
ms_receipt_data = ms_receipt_data[~ms_receipt_data.index.duplicated(keep='first')]

#HS Physical Stock
ms_physical_stock = data_df['HS Physical Stock']

ms_testing = 10

ms_total = (data_df['MS Physical Stock'].shift(1)+ ms_receipt_data )
ms_actual_nozzle_sales  = ms_total_nozzle_sales - ms_testing
ms_closing_stock = ms_actual_nozzle_sales - ms_total
ms_loss_gain_stock = data_df['HS Stock Volume'] - ms_closing_stock



##---------------------------------XP----------------------------------------------------

# XP Nozzle Sales 
data_df['XP Nozzle 1'] = clean_numeric_data(data_df['XP Nozzle 1'])
# Calculate the difference between consecutive days for each nozzle
xp_nozzle1_diff = data_df['XP Nozzle 1'].diff().shift(-1)


# HS Calculate the total nozzle sales for each day
xp_total_nozzle_sales = (xp_nozzle1_diff + xp_nozzle1_diff).fillna(0)
data_df['XP Nozzle 1'] = clean_numeric_data(data_df['XP Nozzle 1'])
data_df['XP Stock Volume'] = clean_numeric_data(data_df['XP Stock Volume'])
data_df['XP Physical Stock'] = clean_numeric_data(data_df['XP Stock Volume'])
data_df['XP Opening Stock'] = data_df['XP Physical Stock'].shift(1)

# Fetching receipt data from 'tdata_df'
xp_receipt_data = tdata_df.set_index('Date')['XP in Litres']

# Ensure the index of receipt_data is unique
xp_receipt_data = xp_receipt_data[~xp_receipt_data.index.duplicated(keep='first')]

xp_physical_stock = data_df['XP Physical Stock']
xp_stock_volume = data_df['XP Stock Volume']

xp_testing = 5

xp_total = (data_df['MS Physical Stock'].shift(1)+ xp_receipt_data )
xp_actual_nozzle_sales  = xp_total_nozzle_sales - xp_testing
xp_closing_stock = xp_actual_nozzle_sales - xp_total
xp_loss_gain_stock = data_df['XP Stock Volume'] - xp_closing_stock




#----------------------------------------------------------------------------------------

# Add the 'HS_Total Nozzle sales' column to the DataFrame
data_df['HS_Actual Nozzle sales'] = hs_actual_nozzle_sales
data_df['MS_Actual Nozzle sales'] = ms_actual_nozzle_sales
data_df['XP_Actual Nozzle sales'] = xp_actual_nozzle_sales


# Create separate DataFrames for HS, MS, and XP
# Create separate DataFrame for HS
hs_cal = pd.DataFrame({
    "Date": data_df["Date"],
    "DIP": data_df["HS DIP"],
    "HS Nozzle 1": data_df["HS Nozzle 1"].map('{:.2f}'.format),
    "HS Nozzle 2": data_df["HS Nozzle 2"].map('{:.2f}'.format),
    "HS Nozzle 3": data_df["HS Nozzle 3"].map('{:.2f}'.format),
    "HS_Total Nozzle sales": hs_total_nozzle_sales.map('{:.2f}'.format),
    "HS Stock Volume": hs_stock_volume.map('{:.2f}'.format),
    "HS Physical Volume": hs_physical_stock.map('{:.2f}'.format),
    "HS Opening Stock": data_df['HS Physical Stock'].shift(1).map('{:.2f}'.format),
    "HS Receipt": hs_receipt_data.replace("<NA>", pd.NA).fillna(0).map('{:.2f}'.format),
    "HS Actual Nozzle Sales": hs_actual_nozzle_sales.map('{:.2f}'.format),
    "HS Closing Stock": hs_closing_stock.map('{:.2f}'.format),
    "HS Loss / Gain": hs_loss_gain_stock.map('{:.2f}'.format)
})

ms_cal = pd.DataFrame({
    "Date": data_df["Date"],
    "DIP": data_df["MS DIP"],
    "MS Nozzle 1": data_df["MS Nozzle 1"],
    "MS Nozzle 2": data_df["MS Nozzle 2"],
    "MS_Total Nozzle sales": ms_total_nozzle_sales,
    "MS Stock Volume": ms_stock_volume,
    "MS Physical Volume": ms_physical_stock,
    "MS Opening Stock": data_df['MS Physical Stock'].shift(1),
    "MS Receipt": ms_receipt_data,
    "MS Actual Nozzle Sales": ms_actual_nozzle_sales,
    "MS Closing Stock": ms_closing_stock,
    "MS Loss / Gain": ms_loss_gain_stock
})


xp_cal = pd.DataFrame({
    "Date": data_df["Date"],
    "DIP": data_df["XP DIP"],
    "XP Nozzle 1": data_df["XP Nozzle 1"],
    "XP_Total Nozzle sales": xp_total_nozzle_sales,
    "XP Stock Volume": xp_stock_volume,
    "XP Physical Volume": xp_physical_stock,
    "XP Opening Stock": data_df['XP Physical Stock'].shift(1),
    "XP Receipt": xp_receipt_data,
    "XP Actual Nozzle Sales": xp_actual_nozzle_sales,
    "XP Closing Stock": xp_closing_stock,
    "XP Loss / Gain": xp_loss_gain_stock
})

# Display the tables in Streamlit
st.subheader("HS Nozzle Data")
st.table(hs_cal)

st.subheader("MS Nozzle Data")
st.table(ms_cal)

st.subheader("XP Nozzle Data")
st.table(xp_cal)



# Save data to CSV files
output_folder = "./data/"

# Check if the 'data' folder exists, create it if not
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Save dataframes to CSV files
hs_cal.to_csv(os.path.join(output_folder, "hs_data.csv"), index=False)
ms_cal.to_csv(os.path.join(output_folder, "ms_data.csv"), index=False)
xp_cal.to_csv(os.path.join(output_folder, "xp_data.csv"), index=False)