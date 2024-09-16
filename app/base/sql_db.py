from tortoise import Tortoise

from app.base.config import config
from app.utils.sql_db import load_modules


async def init_postgres_connection(
    connection_type: str,
    user: str,
    password: str,
    host: str,
    port: int,
    database: str,
    **kwargs,
) -> None:
    connection_url = f"{connection_type}://{user}:{password}@{host}:{port}/{database}?maxsize={config['database']['pool_size']}"
    await Tortoise.init(
        db_url=connection_url, modules={"app": load_modules('app')}, **kwargs
    )

async def generate_schemas() -> None:
    await Tortoise.generate_schemas()
