from fastapi import FastAPI

from atlas_app.api.v1.api import router
from atlas_app.service.db import database

app = FastAPI(
    title="Altana-Atlas-API",
    version="1.0",
    description="Altana Atlas APi on FastAPI",
)


@app.get("/")
async def root():
    return {"message`": "This is Altana Atlas App!"}


@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()

app.include_router(router, prefix="/api/v1")
