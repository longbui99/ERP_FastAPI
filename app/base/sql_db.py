from tortoise import Tortoise


async def init_postgres_connection(
    connection_type: str,
    user: str,
    password: str,
    host: str,
    port: int,
    database: str,
    **kwargs,
) -> None:
    connection_url = f"{connection_type}://{user}:{password}@{host}:{port}/{database}"
    await Tortoise.init(
        db_url=connection_url, modules={"app": ["app.models.users"]}, **kwargs
    )

async def generate_schemas():
    await Tortoise.generate_schemas()
