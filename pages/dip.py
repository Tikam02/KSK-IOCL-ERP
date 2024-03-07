import streamlit as st
import pandas as pd
import numpy as np
import math


def convert_dip_to_volume(dip, data):
    try:
        # Ensure 'DIP' column contains numeric values
        if not pd.to_numeric(data['DIP'], errors='coerce').notna().all():
            st.error("Error: 'DIP' column must contain numeric values.")
            return

        # Find the closest row based on the dip
        filtered_data = data[data['DIP'] == int(dip)]

        if not filtered_data.empty:
            closest_row = filtered_data.iloc[0]

            # Ensure 'DIFF' and 'VOLUME' columns contain numeric values
            try:
                diff_value = float(closest_row['DIFF'])
                volume_value = float(closest_row['VOLUME'])

                # Calculate the final volume
                dip_int = int(dip)
                dip_decimal = (dip % 1) * 10
                calculate_difference = dip_decimal * diff_value
                final_stock_volume = volume_value + calculate_difference

                # Display the final volume
                st.success(f'Final Volume: {final_stock_volume:.2f}')
            except ValueError:
                st.error("Error: 'DIFF' and 'VOLUME' columns must contain numeric values.")
        else:
            # Display an error if the dip is not found
            st.error('Error: Dip value not found in the table.')
    except Exception as e:
        st.error(f'Error fetching or processing data: {e}')

  


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
