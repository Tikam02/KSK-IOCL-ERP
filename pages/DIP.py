import streamlit as st
import pandas as pd
import numpy as np
import math



def convert_dip_to_volume(dip, data):
    try:
        # Ensure 'DIP' column contains numeric values
        data['DIP'] = pd.to_numeric(data['DIP'], errors='coerce')

        # Find the closest row based on the dip
        closest_row = data.loc[(data['DIP'] - dip).abs().idxmin()]

        # Ensure 'DIFF' and 'VOLUME' columns contain numeric values
        diff_value = pd.to_numeric(closest_row['DIFF'], errors='coerce')
        volume_value = pd.to_numeric(closest_row['VOLUME'], errors='coerce')

        # Calculate the final volume
        dip_int = int(dip)
        dip_decimal = (dip % 1) * 10
        calculate_difference = dip_decimal * diff_value
        final_stock_volume = volume_value + calculate_difference

        # Display the final volume
        st.success(f'Final Volume: {final_stock_volume:.2f}')

        return final_stock_volume

    except Exception as e:
        st.error(f'Error fetching or processing data: {e}')
        return None

def main():
    st.title('Dip to Volume Converter')

    # Load CSV data
    data = pd.read_csv('./c_chart.csv')  # Update with your actual CSV file path

    # Input form
    dip_input = st.number_input('Enter Dip:', step=0.1, key='dip_input')
    convert_button = st.button('Convert', key='convert_button')

    # Perform conversion when the button is clicked
    if convert_button:
        convert_dip_to_volume(dip_input, data)

if __name__ == '__main__':
    main()
