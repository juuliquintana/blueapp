import streamlit as st
from streamlit import config
# Configurar el tema de colores
theme = {
    "primaryColor": "#0090DA",
    "backgroundColor": "#FFFFFF",
    "secondaryBackgroundColor": "#7FADE3",
    "textColor": "#1F2A44",
    "font": "verdana"
}
st.set_page_config(page_title="New Campaign Evaluation", layout="centered")
st.markdown(
    f"""
    <style>
        body {{
            color: {theme['textColor']};
            background-color: {theme['backgroundColor']};
        }}
        .sidebar .sidebar-content {{
            background-color: {theme['secondaryBackgroundColor']};
        }}
        .stButton>button {{
            color: white;
            background-color: {"#0090DA"};
            border-radius: 5px;
        }}
        .stNumberInput>div>div>input {{
            border-radius: 5px;
            border: 1px solid {"#0090DA"};
        }}
    </style>
    """,
    unsafe_allow_html=True
)
st.sidebar.image("Logo_blue.png", use_container_width=True)
selected_tab = st.sidebar.radio("",["New Campaign Evaluation", "Testing Campaigns"])
if selected_tab == "New Campaign Evaluation":
    st.title("New Campaign Evaluation")
    sales = st.number_input("Sales per day (provided by client):", min_value=0, value=0, step=1)
    revenue = st.number_input("Average revenue per sale (provided by client):", min_value=0.0, value=0.0, step=0.01)
    moneda = st.selectbox("Select Currency:", ["USD", "GBP", "RUB", "DKK", "NOK", "SEK", "EUR"])
    conversion_share = st.selectbox("Select Country:", ['Scandinavia', 'Rest of Europe', 'USA and WW'])
    tipo_conversion_share = {'Scandinavia': 5.4, 'Rest of Europe': 4.12, 'USA and WW': 3.67}
    commission = st.number_input("Commission (%):", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    
    tipo_cambio = {
        ("USD", "EUR"): 0.9602, ("GBP", "EUR"): 1.1936,
        ("RUB", "EUR"): 0.0098, ("DKK", "EUR"): 0.130,
        ("NOK", "EUR"): 0.085, ("SEK", "EUR"): 0.087, ("EUR", "EUR"): 1.0
    }
        
    if st.button("Calculate"):
        conversion_share_decimal = tipo_conversion_share.get(conversion_share) / 100
        commission_decimal = commission / 100
        potential_revenue = (sales * conversion_share_decimal) * revenue * commission_decimal * 30
        potential_revenue_converted = potential_revenue * tipo_cambio.get((moneda, "EUR"), 1.0)
        st.success(f"Potential revenue: {potential_revenue_converted:,.2f} EUR")

elif selected_tab == "Testing Campaigns":
    st.title("Testing Campaigns")
    media_cost = st.number_input("Accumulated media cost (EUR):", min_value=0.0, max_value=100000.0, value=0.0, step=0.1)
    days = st.number_input("Days of testing:", min_value=0, value=0, step=1)
    if st.button("Calculate"):
        if days > 0:
            potential_revenue_test = (media_cost / days) * 30
            st.success(f"Potential media coast: {potential_revenue_test:,.2f} EUR")
        else:
            st.error("The number of days must be greater than 0 to calculate the average cost.")


            
