import streamlit as st
import pandas as pd

# Function to display the form to enter important dates
def add_event():
    st.subheader("Add Event")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    deadline = st.date_input("Deadline")
    description = st.text_area("Description")
    amount_needed = st.number_input("Amount Needed (Optional)", min_value=0.0)
    if st.button("Add Event"):
        # Save the entered data to a DataFrame or database
        # Here, I'm just displaying the entered data
        st.success("Event Added Successfully!")
        st.write("Start Date:", start_date)
        st.write("End Date:", end_date)
        st.write("Deadline:", deadline)
        st.write("Description:", description)
        if amount_needed:
            st.write("Amount Needed:", amount_needed)

# Function to display all events
def view_events():
    st.subheader("View Events")
    # Load events data from a DataFrame or database
    # Here, I'm just displaying a static DataFrame for demonstration
    events_data = pd.DataFrame({
        "Start Date": ["2024-03-15", "2024-03-20"],
        "End Date": ["2024-03-18", "2024-03-25"],
        "Deadline": ["2024-03-17", "2024-03-22"],
        "Description": ["Project Presentation", "Client Meeting"],
        "Amount Needed": [5000.0, None]
    })
    st.dataframe(events_data)

# Main function to run the Streamlit app
def main():
    st.title("Important Dates Management")
    add_event()
    view_events()

if __name__ == "__main__":
    main()
