import streamlit as st

from app.models.house import House
from app.utils.geo import melb_lat_lng
from app.enums.house import LocationType, Months, WeekOfDay, HouseType
from app.services.house import predict_price
from streamlit_extras.row import row 

# Set the page title
st.set_page_config(
    page_title="Predict House Prices",
    layout="wide"
)

# Display a title
st.title("Welcome to Predict House Prices!")

house =  House()

if 'house_predict' not in st.session_state:
    st.session_state.house_predict = house

house = st.session_state.house_predict

def convert_to_float(val_str, val_default = 0):
    try:
        return float(val_str)
    except:
        return val_default

def render_house_location():
    loc_options = [item.value for item in LocationType]
    house.selected_location_type = st.radio(
        "How do you want to input the house location?",
        loc_options,
        index=0,
    )

    c1, c2, c3,c4 = st.columns([1,1,1,2])  

    is_disabled = house.selected_location_type != LocationType.GEO_LOC

    if house.selected_location_type == LocationType.ADDRESS:   
               
        with c4:
            house.address = st.text_input("Address", house.address, key="Address")
            if st.button("Get Geo Locations", key="get-location"):
                try:
                    house.address_to_lat_lng()
                    house.get_distance_from_cbd()
                except:
                    st.error("An error occured, please retry or check your address.")
    with c1:
        house.latitude = st.text_input("Latitude", house.latitude, key="Latitude", disabled=is_disabled)
        if st.button("Predict Price"):
            house.price = predict_price(house)
            st.success(f"House Price is: {house.price:,.0f} $")
    with c2:
        house.longitude = st.text_input("Longitude", house.longitude, key="Longitude", disabled=is_disabled)
    with c3:
        st.text("")        
        st.info(f"Distance: {house.distance:.2f} km")
    
    


def render_other_inputs():
    house_options = [item.name.title() for item in HouseType]
    selected_house_type = st.selectbox("House Type", house_options, index=0, key="house-type")
    house.set_house_type(selected_house_type)

    c1, c2, c3 = st.columns([1,1,1])
    with c1:
        house.bathroom = st.number_input("Bathroom", min_value=0, max_value=5, value=house.bathroom, key="bathroom")
    with c2:
        house.car = st.number_input("Car Park", min_value=0, max_value=5, value=house.car, key="car")
    with c3:
        house.rooms = st.number_input("Rooms", min_value=0, max_value=5, value=house.rooms, key="rooms")

    c1, c2 = st.columns([1,1])
    with c1:
        house.landsize = st.number_input("Landsize", min_value=100, value=house.landsize, key="landsize")
    with c2:
        house.building_area = st.number_input("Building Area", min_value=0, max_value=house.landsize, value=house.building_area, key="building_area")
    
    c1, c2 = st.columns([1,1])
    with c1:
        house.year_built = st.number_input("Built Year", min_value=1930, max_value=2021, value=house.year_built, key="year_built")
    with c2:
        house.year = st.number_input("Sold Year", min_value=house.year_built, max_value=2021, value=house.year, key="year")
    
    c1, c2 = st.columns([1,1])
    with c1:
        month_options = [item.name.title() for item in Months]
        selected_month_type = st.selectbox("Month", month_options, index=0, key="month-type")
        house.set_month(Months[selected_month_type.upper()])

    with c2:
        day_options = [item.name.title() for item in WeekOfDay]
        selected_day = st.selectbox("Day of the Week", day_options, index=0, key="day-type")
        house.set_day(WeekOfDay[selected_day.upper()])




render_house_location()
with st.sidebar:
    render_other_inputs()