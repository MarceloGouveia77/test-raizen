import src.app.main as main
from src.db.models import Weather


class WeatherRepository():
    def __init__(self):
        self.model = Weather
        self.db = main.app.state.mongo_collection["weather"]

    async def find_by_city(self, city, date):
        return await self.db.find_one({
            "city": city, 
            "request_date": date}, 
            {'_id': 0}
        )
        
    async def insert(self, data):
        return await self.db.insert_one(data)