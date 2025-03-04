
import streamlit as st
from module_function import *
import warnings

warnings.filterwarnings("ignore")

def num_in(label_str, minimum, maximum):
    return st.number_input(
        f"Enter the Value of {label_str} (Min: {minimum} / Max: {maximum})",
        min_value=minimum, max_value=minimum)

# Streamlit app setup
st.set_page_config(layout="wide")

st.title("SINGAPORE RESALE FLAT PRICES PREDICTING")
st.write("")

col1, col2 = st.columns(2)
with col1:
    year = st.selectbox("Select the Year", json_data['years'])
    town = st.selectbox("Select the Town", json_data['town'])
    flat_type = st.selectbox("Select the Flat Type", json_data['flat_type'])
    flr_area_sqm = num_in("Floor Area sqm", 31.0, 280.0)
    flat_model = st.selectbox("Select the Flat Model", json_data['flat_model'])

with (col2):

    storey_start = num_in("Storey Range Start",1.0, 51.0)
    storey_end = num_in("Storey Range End", 1.0, 51.0)
    re_les_year = num_in("Remaining Lease Year", 1, 99)
    remaining_lease_month = num_in("Remaining Lease Month", 1, 12)
    lease_commence_date = num_in("Lease Commence Date", 1966, 2023)

    if st.button("Predict"):
        price = predict_price(year=year, town=town, flat_type=flat_type,
                              floor_area_sqm=flr_area_sqm, flat_model=flat_model,
                              storey_start=storey_start, storey_end=storey_end,
                              remaining_lease_year=re_les_year, remaining_lease_month=remaining_lease_month,
                              lease_commence_date=lease_commence_date)

        if price is not None:
            st.write(f"**Estimated Resale Price: $ {price}**")
