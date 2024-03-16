import streamlit as st
import pandas as pd
from datetime import datetime
from pages.utils.dip import convert_dip_to_volume



def main():
    local_image_path = "./assets/outlet.png"
    st.image(local_image_path, caption="Your Logo", use_column_width=True,width=200)
    st.markdown("<h1 style='text-align: center; orange: red;'>MAKDI KSK DSR</h1>", unsafe_allow_html=True)


  
    # Date input
    date = st.date_input("**Date**", datetime.now())


   # Load CSV data
    data = pd.read_csv('./c_chart.csv')  # Update with your actual CSV file path


    # HS DIP and Nozzles
    st.header('HS DIP and Nozzle Readings', divider='orange')
    # Input for HS DIP
    hs_dip = st.number_input("**HS DIP**", step=0.01)
    

    # Calculate and display output side by side
    col1, col2 = st.columns(2)  # Create two columns
    # Column 1: Input values
    with col1:
        st.markdown("##### DIP Values")
        st.write(f"HS DIP: {hs_dip}")

    # Column 2: Output field
    with col2:
        st.markdown("##### Stock Litres ")
       # output_value = calculate_output(hs_dip)
        hs_stock_volume = convert_dip_to_volume(hs_dip, data)
        st.write(f"HS Stock Volume: {hs_stock_volume:.2f}" if hs_stock_volume is not None else "HS Stock Volume: N/A")



    # Display and input for HS Nozzle 1
    hs_nozzle1_col, hs_nozzle1_input = st.columns([1, 2])
    hs_nozzle1_col.markdown("###### **HS Nozzle 1**")
    hs_nozzle1 = hs_nozzle1_input.number_input("**Readings**", step=0.01, key="hs_nozzle1_input")
    # Display last entered data for HS Nozzle 1
    last_hs_nozzle1 = get_last_entry("HS Nozzle 1")
    hs_nozzle1_col.text(f"Last entered: {last_hs_nozzle1}")


    # Display and input for HS Nozzle 1
    hs_nozzle2_col, hs_nozzle2_input = st.columns([1, 2])
    hs_nozzle2_col.markdown("###### **HS Nozzle 2**")
    hs_nozzle2 = hs_nozzle2_input.number_input("**Reading**", step=0.01, key="hs_nozzle2_input")
    # Display last entered data for HS Nozzle 1
    last_hs_nozzle2 = get_last_entry("HS Nozzle 2")
    hs_nozzle2_col.text(f"Last entered: {last_hs_nozzle2}")


    # Display and input for HS Nozzle 1
    hs_nozzle3_col, hs_nozzle3_input = st.columns([1, 2])
    hs_nozzle3_col.markdown("###### **HS Nozzle 3**")
    hs_nozzle3 = hs_nozzle3_input.number_input("**Readings**", step=0.01, key="hs_nozzle3_input")
    # Display last entered data for HS Nozzle 3
    last_hs_nozzle3 = get_last_entry("HS Nozzle 3")
    hs_nozzle3_col.text(f"Last entered: {last_hs_nozzle3}")

    st.divider()

    
#----------------------------------------------------------------------------------------------------------------

    # MS DIP and Nozzle 1
    st.header("MS DIP and Nozzle 1")

    # Input for MS DIP
    ms_dip = st.number_input("MS DIP", step=0.01)

    # Calculate and display output side by side
    col1, col2 = st.columns(2)  # Create two columns
    # Column 1: Input values
    with col1:
        st.markdown("##### DIP Values")
        st.write(f"MS DIP: {ms_dip}")

    # Column 2: Output field
    with col2:
        st.markdown("##### Stock Litres ")
       # output_value = calculate_output(hs_dip)
        ms_stock_volume = convert_dip_to_volume(ms_dip, data)
        st.write(f"MS Stock Volume: {ms_stock_volume:.2f}" if ms_stock_volume is not None else "MS Stock Volume: N/A")



    # Display and input for MS Nozzle 1
    ms_nozzle1_col, ms_nozzle1_input = st.columns([1, 2])
    ms_nozzle1_col.markdown("##### MS Nozzle 1")
    ms_nozzle1 = ms_nozzle1_input.number_input("**Readings**", step=0.01, key="ms_nozzle1_input")
    # Display last entered data for MS Nozzle 3
    last_ms_nozzle1 = get_last_entry("MS Nozzle 1")
    ms_nozzle1_col.text(f"Last entered: {last_ms_nozzle1}")


    # Display and input for HS Nozzle 1
    ms_nozzle2_col, ms_nozzle2_input = st.columns([1, 2])
    ms_nozzle2_col.markdown("##### MS Nozzle 2")
    ms_nozzle2 = ms_nozzle2_input.number_input("**Reading**", step=0.01, key="ms_nozzle2_input")
    # Display last entered data for MS Nozzle 2
    last_ms_nozzle2 = get_last_entry("MS Nozzle 2")
    ms_nozzle2_col.text(f"Last entered: {last_ms_nozzle2}")

    st.divider()

##---------------------------------------------------------------------------------------------------------------------------

 
    # XP DIP and Nozzle 1
    st.header("XP DIP and Nozzle 1")

    xp_dip = st.number_input("XP DIP", step=0.01)

    # Calculate and display output side by side
    col1, col2 = st.columns(2)  # Create two columns
    # Column 1: Input values
    with col1:
        st.markdown("##### DIP Values")
        st.write(f"XP DIP: {xp_dip}")

    # Column 2: Output field
    with col2:
        st.markdown("##### Stock Litres ")
       # output_value = calculate_output(hs_dip)
        xp_stock_volume = convert_dip_to_volume(xp_dip, data)
        st.write(f"XP Stock Volume: {xp_stock_volume:.2f}" if xp_stock_volume is not None else "XP Stock Volume: N/A")



    # Display and input for HS Nozzle 1
    xp_nozzle1_col, xp_nozzle1_input = st.columns([1, 2])
    xp_nozzle1_col.markdown("##### XP Nozzle 1")
    xp_nozzle1 = xp_nozzle1_input.number_input("**Reading**", step=0.01, key="xp_nozzle1_input")
    # Display last entered data for XP Nozzle 1
    last_xp_nozzle1 = get_last_entry("XP Nozzle 1")
    xp_nozzle1_col.text(f"Last entered: {last_xp_nozzle1}")


    st.divider()


##-------------------------------------------------------------------------------------------------------------------------------

   # Submit button
    # if st.button("Submit"):
    #     # Prepare data object
    #     data = {
    #         "Date": date,
    #         "HS DIP": hs_dip,
    #         "HS Nozzle 1": hs_nozzle1,
    #         "HS Nozzle 2": hs_nozzle2,
    #         "HS Nozzle 3": hs_nozzle3,
    #         "MS DIP": ms_dip,
    #         "MS Nozzle 1": ms_nozzle1,
    #         "MS Nozzle 2": ms_nozzle2,
    #         "XP DIP": xp_dip,
    #         "XP Nozzle 1": xp_nozzle1,
    #     }

        

    #     # Save data to CSV
    #     save_to_csv(data)

    #     # Display a success message
    #     st.success("Data submitted successfully!")


    # Submit button
    if st.button("Submit"):
        # Check for mandatory fields
        if not all([date, hs_dip, hs_nozzle1, hs_nozzle2, hs_nozzle3, ms_dip, ms_nozzle1, ms_nozzle2, xp_dip, xp_nozzle1]):
            st.warning("All fields are mandatory. Please fill in all the input fields.", icon="⚠️")
            st.toast('Enter All The Data!', icon="🚨")
        else:
            # Prepare data object
            data = {
                "Date": date,
                "HS DIP": hs_dip,
                "HS Nozzle 1": hs_nozzle1,
                "HS Nozzle 2": hs_nozzle2,
                "HS Nozzle 3": hs_nozzle3,
                "MS DIP": ms_dip,
                "MS Nozzle 1": ms_nozzle1,
                "MS Nozzle 2": ms_nozzle2,
                "XP DIP": xp_dip,
                "XP Nozzle 1": xp_nozzle1,
                "HS Stock Volume": hs_stock_volume,
                "MS Stock Volume": ms_stock_volume,
                "XP Stock Volume": xp_stock_volume
            }

            # Save data to CSV
            save_to_csv(data)

            # Display a success message
            st.success("Data submitted successfully!")

            



##-----------------------------------------

def get_last_entry(column_name):
    try:
        df = pd.read_csv("data.csv")
        last_entry = df[column_name].iloc[-1]
        return last_entry
    except (FileNotFoundError, IndexError):
        return ""

def save_to_csv(data):
    # Load existing data from CSV
    try:
        df = pd.read_csv("data.csv")
    except FileNotFoundError:
        # Create a new DataFrame if the file doesn't exist
        df = pd.DataFrame(columns=["Date", "HS DIP", "HS Nozzle 1", "HS Nozzle 2", "HS Nozzle 3",
                                   "MS DIP", "MS Nozzle 1", "MS Nozzle 2", "XP DIP", "XP Nozzle 1",
                                   "HS Stock Volume", "MS Stock Volume", "XP Stock Volume"])

    # Format numbers to have two decimal places before appending the data to the DataFrame
    for key, value in data.items():
        if isinstance(value, float):
            data[key] = "{:.2f}".format(value)

    # Check for None values in the data
    non_none_data = {key: value for key, value in data.items() if value is not None}

    # Append the new data to the DataFrame
    df = df.append(non_none_data, ignore_index=True)

    # Save the entire DataFrame to the CSV file
    df.to_csv("data.csv", index=False)



if __name__ == "__main__":
    main()
