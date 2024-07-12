from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

from func import DB_URL
from models import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("execution before startup")
    await db.set_bind(DB_URL)
    await db.gino.create_all()
    yield print("Execute before closed")


app = FastAPI(title="miac_anketa_api", lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")
