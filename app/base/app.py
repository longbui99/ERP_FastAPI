from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.base.sql_db import *
from app.base.config import config
from app.base.main import load_args

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_postgres_connection(**config['database'])
    yield

app = FastAPI(lifespan=lifespan)