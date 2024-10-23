from enum import Enum

class LocationType(str, Enum):
    ADDRESS = "By address"
    GEO_LOC = "By latitude, longitude"