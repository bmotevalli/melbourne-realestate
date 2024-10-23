from pydantic import BaseModel, Field
from typing import Optional

from app.utils.geo import get_lat_long, calculate_distance

class House(BaseModel):
    rooms         : int             = Field(default = 0, alias='Rooms'        )
    distance      : float           = Field(default = 5, alias='Distance'     )
    bathroom      : int             = Field(default = 0, alias='Bathroom'     )
    car           : int             = Field( default = 0   , alias='Car'          )
    landsize      : float           = Field( default = 100 , alias='Landsize'     )
    building_area : float           = Field( default = 0   , alias='BuildingArea' )
    year_built    : int             = Field( default = 1990, alias='YearBuilt'    )
    latitude      : Optional[float] = Field( default =None , alias='Lattitude'    )
    longitude     : Optional[float] = Field( default =None , alias='Longtitude'   )
    year          : int             = Field( default = 2010, alias='Year'         )
    month         : int             = Field( default = 1   , alias='Month'        )
    day_of_week   : int             = Field( default = 1   , alias='DayOfWeek'    )
    type_h        : int             = Field( default =1    , alias='Type_h'       )
    type_t        : int             = Field( default =0    , alias='Type_t'       )
    type_u        : int             = Field( default =0    , alias='Type_u'       )
    address       : Optional[str]   = Field( default =None , alias='Address'      )
    price         : Optional[float] = Field( default =None , alias='Price'        )

    # age_at_sale   : int             = Field(               alias='AgeAtSale'    )

    @property
    def age_at_sale(self):
        return self.year - self.year_built

    def address_to_lat_lng(self):
        if self.address:
            self.latitude, self.longitude = get_lat_long(self.address)

    def get_distance_from_cbd(self):
        lat_cbd, lng_cbd = get_lat_long("Melbourne, VIC")
        if self.latitude and self.longitude:
            self.distance = calculate_distance(lat_cbd, lng_cbd, self.latitude, self.longitude)

