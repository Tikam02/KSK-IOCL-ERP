# import streamlit as st
# import pandas as pd
# import numpy as np
# import math



# def convert_dip_to_volume(dip, data):
#     try:
#         # Ensure 'DIP' column contains numeric values
#         data['DIP'] = pd.to_numeric(data['DIP'], errors='coerce')

#         # Find the closest row based on the dip
#         closest_row = data.loc[(data['DIP'] - dip).abs().idxmin()]

#         # Ensure 'DIFF' and 'VOLUME' columns contain numeric values
#         diff_value = pd.to_numeric(closest_row['DIFF'], errors='coerce')
#         volume_value = pd.to_numeric(closest_row['VOLUME'], errors='coerce')

#         # Calculate the final volume
#         dip_int = int(dip)
#         dip_decimal = (dip % 1) * 10
#         calculate_difference = dip_decimal * diff_value
#         final_stock_volume = volume_value + calculate_difference

#         # Display the final volume
#         st.success(f'Final Volume: {final_stock_volume:.2f}')

#         return final_stock_volume

#     except Exception as e:
#         st.error(f'Error fetching or processing data: {e}')
#         return None

# def main():
#     st.title('Dip to Volume Converter')

#     # Load CSV data
#     data = pd.read_csv('./c_chart.csv')  # Update with your actual CSV file path

#     # Input form
#     dip_input = st.number_input('Enter Dip:', step=0.1, key='dip_input')
#     convert_button = st.button('Convert', key='convert_button')

#     # Perform conversion when the button is clicked
#     if convert_button:
#         convert_dip_to_volume(dip_input, data)

# if __name__ == '__main__':
#     main()


# import streamlit as st
# import pandas as pd


# @st.cache_data
# def convert_dip_to_volume(dip, data):
#     try:
#         # Ensure 'DIP' column contains numeric values
#         data['DIP'] = pd.to_numeric(data['DIP'], errors='coerce')

#         # Find the exact row based on the dip
#         exact_row = data[data['DIP'] == dip]

#         if not exact_row.empty:
#             # Ensure 'VOLUME' and 'DIFF' columns contain numeric values
#             volume_value = pd.to_numeric(exact_row['VOLUME'], errors='coerce')
#             diff_value = pd.to_numeric(exact_row['DIFF'], errors='coerce')

#             # Calculate the final volume
#             dip_int = int(dip)
#             dip_decimal = (dip % 1) * 10
#             calculate_difference = dip_decimal * diff_value.values[0]
#             final_stock_volume = volume_value.values[0] + calculate_difference

#             return final_stock_volume
#         else:
#             return None  # DIP value not found in the CSV file

#     except Exception as e:
#         raise ValueError(f'Error fetching or processing data: {e}')


# def main():
#     st.title('Dip to Volume Converter')

#     # Load CSV data
#     data = pd.read_csv('./c_chart.csv')  # Update with your actual CSV file path

#     # Input form
#     dip_input = st.number_input('Enter Dip:', step=0.1, key='dip_input')
#     convert_button = st.button('Convert', key='convert_button')

#     # Perform conversion when the button is clicked
#     if convert_button:
#         final_volume = convert_dip_to_volume(dip_input, data)
#         if final_volume is not None:
#             st.success(f'Final Volume: {final_volume:.2f}')
#         else:
#             st.error("DIP value not found in the CSV file.")


# if __name__ == '__main__':
#     main()


import streamlit as st
import json

def calculate_stock_volume(dip, data):
    try:
        # Convert JSON string to Python dictionary
        data_dict = json.loads(data)

        # Convert DIP to integer and decimal parts
        dip_int = int(dip)
        dip_decimal = (dip % 1) * 10

        # Find the closest DIP value in the JSON data
        closest_dip = None
        closest_diff = None
        closest_volume = None
        for entry in data_dict:
            if entry['DIP'] <= dip_int:
                closest_dip = entry['DIP']
                closest_volume = float(entry['VOLUME'])
                closest_diff = float(entry['DIFF'])
            else:
                break

        if closest_dip is not None:
            # Calculate the final stock volume
            calculate_difference = dip_decimal * closest_diff
            final_stock_volume = closest_volume + calculate_difference
            return final_stock_volume
        else:
            raise ValueError("DIP value not found in the JSON data.")

    except Exception as e:
        raise ValueError(f'Error processing data: {e}')

def main():
    st.title("DIP to Volume Converter")

    # Read JSON data from file
    with open("./pages/charts.json", "r") as json_file:
        json_data = json_file.read()

    # User input DIP value
    dip_input = st.number_input("Enter DIP value:", min_value=0.0, step=0.1)

    # Calculate button
    if st.button("Calculate"):
        try:
            final_volume = calculate_stock_volume(dip_input, json_data)
            st.success(f"Final Stock Volume: {final_volume:.2f}")
        except ValueError as ve:
            st.error(ve)

if __name__ == "__main__":
    main()

