import functools
from motor import motor_asyncio

from settings import get_settings

settings = get_settings()
client = None


class DatabaseConfiguration:
    client: motor_asyncio.AsyncIOMotorClient = None
    product_collection = None
    async def open(self):
        self.client = motor_asyncio.AsyncIOMotorClient(settings.MONGO_DB_URL)
        self.product_collection = self.client[settings.DB][settings.product_collection]

def start_db():
    def wrapper(func):
        @functools.wraps(func)
        async def async_decorator(*args, **kwargs):
            db_client = DatabaseConfiguration()
            await db_client.open()
            global client
            client = db_client
            return await func(*args, **kwargs)

        return async_decorator

    return wrapper
