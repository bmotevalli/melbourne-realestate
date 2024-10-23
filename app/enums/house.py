from enum import Enum

class LocationType(str, Enum):
    ADDRESS = "By address"
    GEO_LOC = "By latitude, longitude"


class HouseType(str, Enum):
    HOUSE = "House"
    TOWN_HOUSE = "Townhouse"
    UNIT = "Unit"


class WeekOfDay(str, Enum):
    SATURDAY  = 5
    SUNDAY    = 6
    MONDAY    = 0
    TUESDAY   = 1
    WEDNESDAY = 2
    THURSDAY  = 3
    FRIDAY    = 4


class Months(str, Enum):
    JANUARY   = 1
    FEBURARY  = 2
    MARCH     = 3
    APRIL     = 4
    MAY       = 5
    JUNE      = 6
    JULY      = 7
    AUGUST    = 8
    SEPTEMBER = 9
    OCTOBOR   = 10
    NOVEMBER  = 11
    DECEMBER  = 12