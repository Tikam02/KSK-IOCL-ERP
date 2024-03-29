# import streamlit as st
# import pandas as pd
# import numpy as np
# import math
# import json

# def extract_integer_part(number):
#     return int(str(number).split('.')[0][-1])


# def convert_dip_to_volume(dip, data):
#     try:
#         dip_int = int(dip)
#         dip_decimal = (dip - dip_int) * 10
#         ndip_decimal = int(str(dip_decimal).split('.')[0])

#         for entry in data:
#             if entry['DIP'] == dip_int:
#                 volume = float(entry['VOLUME'])
#                 diff = float(entry['DIFF'])
#                 calculate_difference = diff * ndip_decimal
#                 final_stock_volume = volume + calculate_difference
#                 return final_stock_volume

#         raise ValueError("DIP value not found in the JSON data.")

#     except Exception as e:
#         raise ValueError(f'Error processing data: {e}')
    

# # Function to read JSON data from file
# def read_json_file(file_path):
#     with open(file_path, "r") as file:
#         data = json.load(file)
#     return data


# def main():
#     st.title("DIP to Volume Calculator")
    
#     # File path input
#     file_path = "./pages/charts.json"

#     # DIP input
#     dip_input = st.number_input("Enter the DIP value:", step=0.1)

#     # Calculate button
#     if st.button("Calculate"):
#         try:
#             chart_data = read_json_file(file_path)
#             final_volume = convert_dip_to_volume(dip_input, chart_data)
#             st.success(f"Final Stock Volume: {final_volume:.2f}")
#         except ValueError as ve:
#             st.error(ve)

# if __name__ == "__main__":
#     main()


import streamlit as st
import json

def extract_integer_part(number):
    return int(str(number).split('.')[0][-1])

def calculate_stock_volume(dip, data):
    try:
        dip_int = int(dip)
        dip_decimal = (dip - dip_int) * 10
        ndip_decimal = extract_integer_part(dip_decimal)

        for entry in data:
            print("Entry:", entry)  # Debug print
            if entry['DIP'] == dip_int:
                volume = float(entry['VOLUME'])
                diff = float(entry['DIFF'])
                calculate_difference = diff * ndip_decimal
                final_stock_volume = volume + calculate_difference
                return final_stock_volume

        raise ValueError("DIP value not found in the JSON data.")

    except Exception as e:
        raise ValueError(f'Error processing data: {e}')

# Function to read JSON data from file
def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def main():
    st.title("DIP to Volume Calculator")

    #File path input
    file_path = "./pages/charts.json"


    try:
        data = pd.read_json(file_path)
        return data
    except Exception as e:
        raise ValueError(f'Error reading JSON file: {e}')
    

    # DIP input
    dip_input = st.number_input("Enter the DIP value:", step=0.1)

        # Input form
    dip_input = st.number_input('Enter Dip:', step=0.1, key='dip_input')
    convert_button = st.button('Convert', key='convert_button')

        # Perform conversion when the button is clicked
    if convert_button:
        convert_dip_to_volume(dip_input, data)

if __name__ == "__main__":
    main()