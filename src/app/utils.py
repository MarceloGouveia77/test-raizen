from motor.motor_asyncio import AsyncIOMotorClient
from unidecode import unidecode

async def init_mongo(db_name: str, db_url: str, collection: str):
    mongo_client = AsyncIOMotorClient(db_url)
    mongo_database = mongo_client[db_name]
    
    mongo_collections = {
        collection: mongo_database.get_collection(collection),
    }
    return mongo_client, mongo_database, mongo_collections

def normalize_string(string: str):
    return unidecode(string).lower()