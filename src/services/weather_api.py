import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class WeatherApi:
    def __init__(self, city):
        self.api_key = os.getenv("OPEN_WEATHER_API_KEY")
        self.base_url = "http://api.openweathermap.org/data/2.5/forecast?units=metric&"
        self.city = city
        self.complete_url = self.base_url + "appid=" + self.api_key + "&q=" + self.city

    def get_weather_info(self):
        response = requests.get(self.complete_url)
        data = response.json()
        return {
            'city': self.city,
            'list': data['list'],
            'request_date': datetime.today().date().strftime("%Y-%m-%d")
        }