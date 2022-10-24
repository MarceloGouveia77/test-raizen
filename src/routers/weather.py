from datetime import datetime
from fastapi import APIRouter, HTTPException

from src.app.utils import normalize_string
from src.db.models import ExceptionResponse, Weather
from src.db.repositories import WeatherRepository
from src.services.weather_api import WeatherApi

router = APIRouter()

@router.get("", response_model=Weather, responses={404: {"model": ExceptionResponse}})
async def get_weather_by_city(city: str):
    """
    Endpoint that returns the weather forecast for the next 5 days for a given city.
    """
    city = normalize_string(city)
    today = datetime.today().date().strftime("%Y-%m-%d")
    
    weather_repository = WeatherRepository()
    data = await weather_repository.find_by_city(city, today)
    
    if not data:
        weather_api = WeatherApi(city)
        try:
            data = weather_api.get_weather_and_save()
            await weather_repository.insert(data)
        except:
            raise HTTPException(status_code=404, detail="City not found.")
        
    return data