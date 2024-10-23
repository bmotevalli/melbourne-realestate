from pydantic import BaseModel, Field
from typing import Optional

class House(BaseModel):
    rooms        : int             = Field(              alias='Rooms'       )
    distance     : float           = Field(              alias='Distance'    )
    bathroom     : Optional[int]   = Field(default=None, alias='Bathroom'    )
    car          : Optional[int]   = Field(default=None, alias='Car'         )
    landsize     : Optional[float] = Field(default=None, alias='Landsize'    )
    building_area: Optional[float] = Field(default=None, alias='BuildingArea')
    year_built   : Optional[int]   = Field(default=None, alias='YearBuilt'   )
    latitude     : Optional[float] = Field(default=None, alias='Lattitude'   )
    longitude    : Optional[float] = Field(default=None, alias='Longtitude'  )
    year         : int             = Field(              alias='Year'        )
    month        : int             = Field(              alias='Month'       )
    day_of_week  : int             = Field(              alias='DayOfWeek'   )
    age_at_sale  : Optional[int]   = Field(default=None, alias='AgeAtSale'   )
    type_h       : Optional[int]   = Field(default=None, alias='Type_h'      )
    type_t       : Optional[int]   = Field(default=None, alias='Type_t'      )
    type_u       : Optional[int]   = Field(default=None, alias='Type_u'      )

    
