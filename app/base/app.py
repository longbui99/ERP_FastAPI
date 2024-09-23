from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.base.config import config
from app.base.sql_db import init_postgres_connection
from app.base.redis_db import init_redis_connection, rconn
from app.base.main import load_args

@asynccontextmanager
async def lifespan(app: FastAPI):
    load_args()
    dbconfig = config['database']
    await init_postgres_connection(user=dbconfig['user'], password=dbconfig['password'], host=dbconfig['host'], port=dbconfig['port'], database=dbconfig['database'], connection_type=dbconfig['connection_type'])
    rconn.set_connection(init_redis_connection())
    yield

app = FastAPI(lifespan=lifespan)