from geopy.geocoders import Nominatim
import math

melb_lat_lng = [-37.8142454, 144.9631732]

def get_lat_long(address: str):
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="house_geocoder")

    # Geocode the address
    location = geolocator.geocode(address)

    if location:
        return location.latitude, location.longitude
    
    raise ValueError(f"The addres could not be located: {address}")


def calculate_distance(lat, lon):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat)
    lon1_rad = math.radians(lon)
    lat2_rad = math.radians(melb_lat_lng[0])
    lon2_rad = math.radians(melb_lat_lng[1])

    # Differences in coordinates
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c
    return distance