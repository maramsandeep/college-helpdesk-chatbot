from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from typing import Optional


_client: Optional[AsyncIOMotorClient] = None


async def init_db(app: FastAPI, uri: str, db_name: str):
    global _client
    _client = AsyncIOMotorClient(uri)
    app.state.mongo_client = _client
    app.state.db = _client[db_name]


async def close_db(app: FastAPI):
    client: AsyncIOMotorClient = getattr(app.state, "mongo_client", None)
    if client:
        client.close()


# Dependency to access the DB inside routes/services
async def get_db(request) -> "AsyncIOMotorClient":
    return request.app.state.db