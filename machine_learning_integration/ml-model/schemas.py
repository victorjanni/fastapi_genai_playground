from pydantic import BaseModel, Field, StrictInt

class InputSchmema(BaseModel):
    Longitude: float
    latitude: float
    housing_median_age: int = Field(..., gt= 0)
    total_rooms: StrictInt = Field(..., gt=0)
    total_bedrooms: StrictInt = Field(..., gt=0)
    population: int = Field(..., gt=0)
    households: StrictInt = Field(..., gt=0)
    median_income: float = Field(..., gt=0)

class outputSchema(BaseModel):
    predicted_price: float    