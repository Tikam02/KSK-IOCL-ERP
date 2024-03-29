import json
import streamlit as st

def extract_integer_part(number):
    return int(str(number).split('.')[1])

def calculate_stock_volume(dip, data):
    try:
        dip = float(dip)  # Convert input dip to float
        dip_int = int(dip)
        ndip_decimal = extract_integer_part(dip)
        # print("DIP",dip)
        # print("DIP INT",dip_int)
        # print("nDIP",ndip_decimal)

        for entry in data:
            if entry['DIP'] == dip_int:
                volume = float(entry['VOLUME'])
                diff = float(entry['DIFF'])
                calculate_difference = diff * ndip_decimal
                final_stock_volume = volume + calculate_difference
                return final_stock_volume
            
            # print("Volume",volume)
            # print("DIFF",diff)
            # print("Calculate DIFF",calculate_difference)
            # print("Final",final_stock_volume)

        raise ValueError("DIP value not found in the JSON data.")

    except Exception as e:
        raise ValueError(f'Error processing data: {e}')

def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def main():
    st.title("DIP to Volume Calculator")
    
    # File path input
    file_path = "./pages/charts.json"

    # DIP input
    dip_input = st.number_input("Enter the DIP value:", step=0.1)

    # Calculate button
    if st.button("Calculate"):
        try:
            chart_data = read_json_file(file_path)
            final_volume = calculate_stock_volume(dip_input, chart_data)
            st.success(f"Final Stock Volume: {final_volume:.2f}")
        except ValueError as ve:
            st.error(ve)

if __name__ == "__main__":
    main()
