from typing import Annotated

from fastapi import Body

from app import app
from app.base.sql_db import *
from app.utils.sql_db import *
from app.base.exceptions import ClientMethodNotAllowed



@app.get('/database/upgrade')
async def upgrade_database():
    await generate_schemas()

@app.post('/database/create')
async def create_database(dbname: Annotated[str, Body()], master_password: Annotated[str, Body()]):
    database_master_password = get_database_admin_password()
    if master_password != database_master_password:
        raise ClientMethodNotAllowed("Database Master Password is incorrect")
    conn = Tortoise.get_connection('default')
    await conn.execute_query(f'CREATE DATABASE {dbname};')