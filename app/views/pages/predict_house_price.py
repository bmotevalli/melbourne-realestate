import streamlit as st

from app.models.house import House
from app.utils.geo import melb_lat_lng

# Set the page title
st.set_page_config(
    page_title="Predict House Prices",
    layout="wide"
)

# Display a title
st.title("Welcome to Predict House Prices!")

house =  House()

def render_house_location():
    house.selected_location_type = st.radio(
        "How do you want to input the house location?",
        ["By latitude, longitude", "By address"],
        index=None,
    )

    is_disabled = house.selected_location_type != "By latitude, longitude"
        
    
    if house.selected_location_type == "By address":
        house.address = st.text_input("Address", house.address, key="Address")

    
        if st.button("Get Geo Locations", key="get-location"):
            try:
                house.address_to_lat_lng()
                house.get_distance_from_cbd()
                # st.write(f"Latitude: {house.latitude}")
                # st.write(f"Longitude: {house.longitude}")
            except:
                st.error("An error occured, please retry or check your address.")

    house.latitude = st.text_input("Latitude", house.latitude, key="Latitude", disabled=is_disabled)
    house.longitude = st.text_input("Longitude", house.longitude, key="Longitude", disabled=is_disabled)
    st.write(f"Distance: {house.distance:.2f} km")


render_house_location()
