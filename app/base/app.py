from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.base.config import config
from app.base.sql_db import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    dbconfig = config['database']
    await init_postgres_connection(user=dbconfig['user'], password=dbconfig['password'], host=dbconfig['host'], port=dbconfig['port'], database=dbconfig['database'], connection_type=dbconfig['connection_type'])
    yield

app = FastAPI(lifespan=lifespan)