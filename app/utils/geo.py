from geopy.geocoders import Nominatim

def get_lat_long(address: str):
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="house_geocoder")

    # Geocode the address
    location = geolocator.geocode(address)

    if location:
        return location.latitude, location.longitude
    
    raise ValueError(f"The addres could not be located: {address}")