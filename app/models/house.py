from pydantic import BaseModel, Field
from typing import Optional

from app.utils.geo import get_lat_long, calculate_distance
from app.enums.house import LocationType, HouseType, Months, WeekOfDay

class House(BaseModel):
    rooms         : int             = Field( default = 0                                      , alias='Rooms'        )
    distance      : float           = Field( default = 5                                      , alias='Distance'     )
    bathroom      : int             = Field( default = 0                                      , alias='Bathroom'     )
    car           : int             = Field( default = 0                                      , alias='Car'          )
    landsize      : float           = Field( default = 100                                    , alias='Landsize'     )
    building_area : float           = Field( default = 0                                      , alias='BuildingArea' )
    year_built    : int             = Field( default = 1990                                   , alias='YearBuilt'    )
    latitude      : Optional[float] = Field( default =-37.8276058                             , alias='Lattitude'    )
    longitude     : Optional[float] = Field( default =145.0523839                             , alias='Longtitude'   )
    year          : int             = Field( default = 2010                                   , alias='Year'         )
    month         : int             = Field( default = 1                                      , alias='Month'        )
    day_of_week   : int             = Field( default = 1                                      , alias='DayOfWeek'    )
    type_h        : int             = Field( default =1                                       , alias='Type_h'       )
    type_t        : int             = Field( default =0                                       , alias='Type_t'       )
    type_u        : int             = Field( default =0                                       , alias='Type_u'       )
    address       : Optional[str]   = Field( default ="102 Camberwell Rd, Hawthorn East, VIC" , alias='Address'      )
    price         : Optional[float] = Field( default =None                                    , alias='Price'        )

    selected_location_type: LocationType = LocationType.ADDRESS

    @property
    def age_at_sale(self):
        return self.year - self.year_built

    def address_to_lat_lng(self):
        if self.address:
            self.latitude, self.longitude = get_lat_long(self.address)

    def get_distance_from_cbd(self):
        if self.latitude and self.longitude:
            self.distance = calculate_distance(self.latitude, self.longitude)


    def set_house_type(self, selected_house_type):
        self.type_h = int(selected_house_type == HouseType.HOUSE)
        self.type_t = int(selected_house_type == HouseType.TOWN_HOUSE)
        self.type_u = int(selected_house_type == HouseType.UNIT)

    def set_month(self, selected_month: Months):
        self.month = selected_month.value

    def set_day(self, selected_day: WeekOfDay):
        self.day_of_week = selected_day.value