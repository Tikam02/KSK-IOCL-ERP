import streamlit as st

def main():
    local_image_path = "./assets/iocl.png"

    st.image(local_image_path, use_column_width=True, width=200)
    st.markdown("<h1 style='text-align: center; color: orange;'>Makdi KSK IOCL </h1>", unsafe_allow_html=True)

    st.markdown("Welcome to the Transport Operations main page!")
    # Link to Transport Operations Page
    transport_ops_link = st.markdown("[Transport Operations Page](#transport_ops)")

    # Transport Operations Section
    st.header("Transport Operations Section")
    st.markdown("This is the Transport Operations Section.")

    # Internal link target
    st.markdown("<a id='transport_ops'></a>", unsafe_allow_html=True)

    # Link back to Main Page
    main_page_link = st.markdown("[Back to Main Page](#)")

    
if __name__ == "__main__":
    main()
