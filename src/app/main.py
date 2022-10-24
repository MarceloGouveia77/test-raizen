from fastapi import FastAPI, APIRouter

from src.app import settings
from src.app.utils import init_mongo
from src.routers import weather

initial_settings = settings.get_settings()

app = FastAPI(docs_url="/api/v1/docs", redoc_url="/api/v1/redoc")

app.include_router(weather.router, prefix="/api/v1/weather", tags=["weather"])

@app.on_event("startup")
async def startup_event():
    app.state.mongo_client, app.state.mongo_db, app.state.mongo_collection = await init_mongo(
        initial_settings.db_name, initial_settings.db_url, initial_settings.collection
    )