import streamlit as st

from app.models.house import House
from app.utils.geo import melb_lat_lng
from app.enums.house import LocationType, Months, WeekOfDay, HouseType

# Set the page title
st.set_page_config(
    page_title="Predict House Prices",
    layout="wide"
)

# Display a title
st.title("Welcome to Predict House Prices!")

house =  House()

def render_house_location():
    loc_options = [item.value for item in LocationType]
    house.selected_location_type = st.radio(
        "How do you want to input the house location?",
        loc_options,
        index=0,
    )

    is_disabled = house.selected_location_type != LocationType.GEO_LOC
        
    
    if house.selected_location_type == LocationType.ADDRESS:
        house.address = st.text_input("Address", house.address, key="Address")

    
        if st.button("Get Geo Locations", key="get-location"):
            try:
                house.address_to_lat_lng()
                house.get_distance_from_cbd()
            except:
                st.error("An error occured, please retry or check your address.")

    house.latitude = st.text_input("Latitude", house.latitude, key="Latitude", disabled=is_disabled)
    house.longitude = st.text_input("Longitude", house.longitude, key="Longitude", disabled=is_disabled)
    st.write(f"Distance: {house.distance:.2f} km")




def render_other_inputs():
    house_options = [item.name.title() for item in HouseType]
    selected_house_type = st.selectbox("House Type", house_options, index=0, key="house-type")
    house.set_house_type(selected_house_type)

    house.bathroom = st.number_input("Bathroom", min_value=0, max_value=5, value=house.bathroom, key="bathroom")
    house.car = st.number_input("Car Park", min_value=0, max_value=5, value=house.car, key="car")
    house.rooms = st.number_input("Rooms", min_value=0, max_value=5, value=house.rooms, key="rooms")
    house.landsize = st.text_input("Landsize", value=house.landsize, key="landsize")
    house.building_area = st.text_input("Building Area", value=house.building_area, key="building_area")
    house.year_built = st.text_input("Built Year", value=house.year_built, key="year_built")
    house.year = st.text_input("Sold Year", value=house.year, key="year")
    
    month_options = [item.name.title() for item in Months]
    selected_month_type = st.selectbox("Month", month_options, index=0, key="month-type")
    house.set_month(Months[selected_month_type.upper()])

    day_options = [item.name.title() for item in WeekOfDay]
    selected_day = st.selectbox("Day of the Week", day_options, index=0, key="day-type")
    house.set_day(WeekOfDay[selected_day.upper()])




render_house_location()
render_other_inputs()
