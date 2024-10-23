import streamlit as st

from app.models.house import House

# Set the page title
st.set_page_config(
    page_title="Predict House Prices",
    layout="wide"
)

# Display a title
st.title("Welcome to Predict House Prices!")


house = House()

house.address = st.text_input("Address", house.address)

if st.button("Get Geo Locations"):
    try:
        house.address_to_lat_lng()
        house.get_distance_from_cbd()
        st.write(f"Latitude: {house.latitude}")
        st.write(f"Longitude: {house.longitude}")
        st.write(f"Distance: {house.distance:.2f} km")
    except:
        st.error("An error occured, please retry or check your address.")