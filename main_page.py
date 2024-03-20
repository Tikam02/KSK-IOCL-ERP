import streamlit as st

def main():
    local_image_path = "./assets/iocl.png"

    st.image(local_image_path, use_column_width=True, width=200)
    st.markdown("<h1 style='text-align: center; color: orange;'>Makdi KSK IOCL </h1>", unsafe_allow_html=True)

    st.divider()

    # Link to Transport Operations Page
    st.page_link("pages/dashboard.py",label="Dashboard", icon="📊")
    st.page_link("pages/dsr_cal.py", label="DSR Calculation", icon="⛽️")
    st.page_link("pages/dsr_input.py", label="DSR Entry", icon="🗒")
    st.page_link("pages/expenses.py", label="Expenses / Kharcha", icon="💵")
    st.page_link("pages/transport_ops.py", label="Tanker Entry", icon="🚛")

    st.divider()


    
if __name__ == "__main__":
    main()
