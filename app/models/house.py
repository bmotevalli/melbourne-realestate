from pydantic import BaseModel, Field
from typing import Optional

from app.utils.geo import get_lat_long

class House(BaseModel):
    rooms         : int             = Field(default = 0, alias='Rooms'        )
    distance      : float           = Field(default = 5, alias='Distance'     )
    bathroom      : int             = Field(default = 0, alias='Bathroom'     )
    car           : int             = Field(default = 0,    alias='Car'          )
    landsize      : float           = Field(default = 100,  alias='Landsize'     )
    building_area : float           = Field(default = 0,    alias='BuildingArea' )
    year_built    : int             = Field(default = 2010, alias='YearBuilt'    )
    latitude      : Optional[float] = Field( default=None,  alias='Lattitude'    )
    longitude     : Optional[float] = Field( default=None,  alias='Longtitude'   )
    year          : int             = Field(                alias='Year'         )
    month         : int             = Field(                alias='Month'        )
    day_of_week   : int             = Field(                alias='DayOfWeek'    )
    age_at_sale   : int             = Field(                alias='AgeAtSale'    )
    type_h        : int             = Field(                alias='Type_h'       )
    type_t        : int             = Field(                alias='Type_t'       )
    type_u        : int             = Field(                alias='Type_u'       )
    address       : Optional[str]   = Field(default=None,   alias='Address'      )
    price         : Optional[float] = Field(default=None,   alias='Price'        )


    def address_to_lat_lng(self):
        if self.address:
            self.latitude, self.longitude = get_lat_long(self.address)




