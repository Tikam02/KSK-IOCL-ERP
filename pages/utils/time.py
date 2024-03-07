import streamlit as st
from datetime import datetime

def save_click_time():
    # Get the current time
    current_time = datetime.now()

    # Format the time as a string
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Save the time to a file or database, or use it as needed
    with open('click_times.txt', 'a') as file:
        file.write(f'User clicked submit at: {formatted_time}\n')