from motor.motor_asyncio import AsyncIOMotorClient
from store.core.config import settings
from bson import UuidRepresentation

class MongoCLient:
    def __init__(self) -> None:
        print("MongoCLient", settings.DATABASE_URL)
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(settings.DATABASE_URL)

    def get(self) -> AsyncIOMotorClient:
        return self.client

db_client = MongoCLient()