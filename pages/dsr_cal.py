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
hs_nozzle1_diff = merged_df['HS Nozzle 1'].diff().shift(-1)
hs_nozzle2_diff = merged_df['HS Nozzle 2'].diff().shift(-1)
hs_nozzle3_diff = merged_df['HS Nozzle 3'].diff().shift(-1)



# HS Calculate the total nozzle sales for each day
hs_total_nozzle_sales = (hs_nozzle1_diff + hs_nozzle2_diff + hs_nozzle3_diff).fillna(0)
merged_df['HS Nozzle 1'] = clean_numeric_data(merged_df['HS Nozzle 1'])
merged_df['HS Nozzle 2'] = clean_numeric_data(merged_df['HS Nozzle 2'])
merged_df['HS Nozzle 3'] = clean_numeric_data(merged_df['HS Nozzle 3'])
hs_stock_volume = clean_numeric_data(merged_df['HS Stock Volume'])
merged_df['HS Physical Stock'] = clean_numeric_data(merged_df['HS Stock Volume'])
merged_df['HS Opening Stock'] = merged_df['HS Physical Stock'].shift(1)



#HS Physical Stock
hs_physical_stock = merged_df['HS Physical Stock']
hs_receipt_data = merged_df['HS in Litres']

hs_testing = 10

hs_total_stock = hs_physical_stock + hs_receipt_data 
hs_actual_nozzle_sales  = hs_total_nozzle_sales - hs_testing
hs_closing_stock = hs_actual_nozzle_sales - hs_total_stock
hs_loss_gain_stock = hs_stock_volume - hs_closing_stock


# data_df['Loss_Gain Stock'] = clean_numeric_data(data_df['Loss_Gain Stock'])
# data_df['Cumm LnG Stock'] = clean_numeric_data(data_df['Cumm LnG Stock'])

##-----------------------------------------MS--------------------------------------

# MS Nozzle Sales 
merged_df['MS Nozzle 1'] = clean_numeric_data(merged_df['MS Nozzle 1'])
merged_df['MS Nozzle 2'] = clean_numeric_data(merged_df['MS Nozzle 2'])

# Calculate the difference between consecutive days for each nozzle
ms_nozzle1_diff = data_df['MS Nozzle 1'].diff().shift(-1)
ms_nozzle2_diff = data_df['MS Nozzle 2'].diff().shift(-1)


# HS Calculate the total nozzle sales for each day
ms_total_nozzle_sales = (ms_nozzle1_diff + ms_nozzle2_diff).fillna(0)
merged_df['MS Nozzle 1'] = clean_numeric_data(merged_df['MS Nozzle 1'])
merged_df['MS Nozzle 2'] = clean_numeric_data(merged_df['MS Nozzle 2'])
ms_stock_volume = clean_numeric_data(merged_df['MS Stock Volume'])
merged_df['MS Physical Stock'] = clean_numeric_data(merged_df['MS Stock Volume'])
merged_df['MS Opening Stock'] = merged_df['MS Physical Stock'].shift(1)



ms_physical_stock = merged_df['MS Physical Stock']
ms_receipt_data = merged_df['MS in Litres']

ms_testing = 10

ms_total =  ms_physical_stock + ms_receipt_data 
ms_actual_nozzle_sales  = ms_total_nozzle_sales - ms_testing
ms_closing_stock = ms_actual_nozzle_sales - ms_total
ms_loss_gain_stock = ms_stock_volume - ms_closing_stock



##---------------------------------XP----------------------------------------------------

# XP Nozzle Sales 
merged_df['XP Nozzle 1'] = clean_numeric_data(merged_df['XP Nozzle 1'])
# Calculate the difference between consecutive days for each nozzle
xp_nozzle1_diff = merged_df['XP Nozzle 1'].diff().shift(-1)


# HS Calculate the total nozzle sales for each day
xp_total_nozzle_sales = (xp_nozzle1_diff + xp_nozzle1_diff).fillna(0)
merged_df['XP Nozzle 1'] = clean_numeric_data(merged_df['XP Nozzle 1'])
merged_df['XP Stock Volume'] = clean_numeric_data(merged_df['XP Stock Volume'])
merged_df['XP Physical Stock'] = clean_numeric_data(merged_df['XP Stock Volume'])
merged_df['XP Opening Stock'] = merged_df['XP Physical Stock'].shift(1)


xp_stock_volume = data_df['XP Stock Volume']
xp_physical_stock = merged_df['MS Physical Stock']
xp_receipt_data = merged_df['MS in Litres']

xp_testing = 5

xp_total =  xp_physical_stock + xp_receipt_data
xp_actual_nozzle_sales  = xp_total_nozzle_sales - xp_testing
xp_closing_stock = xp_actual_nozzle_sales - xp_total
xp_loss_gain_stock = merged_df['XP Stock Volume'] - xp_closing_stock




#----------------------------------------------------------------------------------------

# Add the 'HS_Total Nozzle sales' column to the DataFrame
data_df['HS_Actual Nozzle sales'] = hs_actual_nozzle_sales
data_df['MS_Actual Nozzle sales'] = ms_actual_nozzle_sales
data_df['XP_Actual Nozzle sales'] = xp_actual_nozzle_sales


# Create separate DataFrames for HS, MS, and XP
# Create separate DataFrame for HS
hs_cal = pd.DataFrame({
    "Date": data_df["Date"],
    "DIP": data_df["HS DIP"].map('{:.2f}'.format),
    "HS Nozzle 1": data_df["HS Nozzle 1"].map('{:.2f}'.format),
    "HS Nozzle 2": data_df["HS Nozzle 2"].map('{:.2f}'.format),
    "HS Nozzle 3": data_df["HS Nozzle 3"].map('{:.2f}'.format),
    "HS_Total Nozzle sales": hs_total_nozzle_sales.map('{:.2f}'.format),
    "HS Stock Volume": hs_stock_volume.map('{:.2f}'.format),
    "HS Physical Volume": hs_physical_stock.map('{:.2f}'.format),
    "HS Opening Stock": merged_df['HS Physical Stock'].shift(1).map('{:.2f}'.format),
    "HS Receipt": hs_receipt_data.replace("<NA>", pd.NA).fillna(0).map('{:.2f}'.format),
    "HS Actual Nozzle Sales": hs_actual_nozzle_sales.map('{:.2f}'.format),
    "HS Closing Stock": hs_closing_stock.map('{:.2f}'.format),
    "HS Loss / Gain": hs_loss_gain_stock.map('{:.2f}'.format)
})

ms_cal = pd.DataFrame({
    "Date": data_df["Date"],
    "DIP": data_df["MS DIP"].map('{:.2f}'.format),
    "MS Nozzle 1": data_df["MS Nozzle 1"].map('{:.2f}'.format),
    "MS Nozzle 2": data_df["MS Nozzle 2"].map('{:.2f}'.format),
    "MS_Total Nozzle sales": ms_total_nozzle_sales.map('{:.2f}'.format),
    "MS Stock Volume": ms_stock_volume.map('{:.2f}'.format),
    "MS Physical Volume": ms_physical_stock.map('{:.2f}'.format),
    "MS Opening Stock":merged_df['MS Physical Stock'].shift(1).map('{:.2f}'.format),
    "MS Receipt": ms_receipt_data.map('{:.2f}'.format),
    "MS Actual Nozzle Sales": ms_actual_nozzle_sales.map('{:.2f}'.format),
    "MS Closing Stock": ms_closing_stock.map('{:.2f}'.format),
    "MS Loss / Gain": ms_loss_gain_stock.map('{:.2f}'.format)
})


xp_cal = pd.DataFrame({
    "Date": data_df["Date"],
    "DIP": data_df["XP DIP"].map('{:.2f}'.format),
    "XP Nozzle 1": data_df["XP Nozzle 1"].map('{:.2f}'.format),
    "XP_Total Nozzle sales": xp_total_nozzle_sales.map('{:.2f}'.format),
    "XP Stock Volume": xp_stock_volume.map('{:.2f}'.format),
    "XP Physical Volume": xp_physical_stock.map('{:.2f}'.format),
    "XP Opening Stock": merged_df['XP Physical Stock'].shift(1).map('{:.2f}'.format),
    "XP Receipt": xp_receipt_data.map('{:.2f}'.format),
    "XP Actual Nozzle Sales": xp_actual_nozzle_sales.map('{:.2f}'.format),
    "XP Closing Stock": xp_closing_stock.map('{:.2f}'.format),
    "XP Loss / Gain": (xp_loss_gain_stock.map('{:.2f}'.format))
})

# # Display the tables in Streamlit
# st.subheader("HS Nozzle Data")
# st.table(hs_cal)





# Save data to CSV files
output_folder = "./data/"

# Check if the 'data' folder exists, create it if not
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Save dataframes to CSV files
hs_cal.to_csv(os.path.join(output_folder, "hs_data.csv"), index=False)
ms_cal.to_csv(os.path.join(output_folder, "ms_data.csv"), index=False)
xp_cal.to_csv(os.path.join(output_folder, "xp_data.csv"), index=False)


def show_data():
    st.title("Show All Data")

    try:
        st.header("All Data")
        # Use st.dataframe instead of st.write for pagination
        st.dataframe(merged_df, width=1200)

        st.subheader("HS Nozzle Data")
        st.dataframe(hs_cal, width=1000)

        st.subheader("MS Nozzle Data")
        st.dataframe(ms_cal, width=1000)

        st.subheader("XP Nozzle Data")
        st.dataframe(xp_cal, width=1000)

    except FileNotFoundError:
        st.error("Data file 'data.csv' not found. No data available.")

    except pd.errors.EmptyDataError:
        st.warning("Data file 'data.csv' is empty. No data available.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    show_data()

