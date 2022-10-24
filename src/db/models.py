from typing import List
from pydantic import BaseModel, Field
from bson import ObjectId

class WeatherListObject(BaseModel):
    dt: int = Field(..., example=1666591200)
    main: dict = Field(..., example={'temp': 24.53, 'feels_like': 24.89, 'temp_min': 24.53, 'temp_max': 25.74, 'pressure': 1017, 'sea_level': 1017, 'grnd_level': 1016, 'humidity': 71, 'temp_kf': -1.21})
    weather: List[dict] = Field(..., example=[{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}])
    clouds: dict = Field(..., example={'all': 16})
    wind: dict = Field(..., example={'speed': 3.76, 'deg': 70, 'gust': 5.1})
    visibility: int = Field(..., example=10000)
    pop: float = Field(..., example=0)
    sys: dict = Field(..., example={'pod': 'n'})
    dt_txt: str = Field(..., example='2022-10-24 06:00:00')

class Weather(BaseModel):
    request_date: str = Field(..., example='2022-10-24')
    city: str = Field(..., example='São Paulo')
    list: List[WeatherListObject]
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        
class ExceptionResponse(BaseModel):
    detail: str = Field(..., example='City not found.')
    status_code: int = Field(..., example=404)