import os
from functools import lru_cache
from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "local")

    db_url: str = os.getenv("MONGO_URL", "")
    db_name: str = os.getenv("MONGO_DB", "")
    collection: str = os.getenv("MONGO_COLLECTION", "")
    test_db_name: str = os.getenv("MONGO_TEST_DB", "")
    
    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()