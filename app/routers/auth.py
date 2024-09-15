from typing import Annotated, List

from fastapi import Form, Depends, Body
from tortoise import Tortoise

from app import app
from app.base.config import config
from app.models.login import LoginCredential
from app.models.users import User, _User
from app.utils.jwt import encode_login_to_jwt


async def _login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    login = LoginCredential(username=username, password=password)

@app.get('/login')
def get_login(login: Annotated[LoginCredential, Depends(_login)]):
    return encode_login_to_jwt(login)

@app.post('/sign-up', response_model=User)
async def signup(username: Annotated[str, Body()], password: Annotated[str, Body()]):
    user = await _User.create(login=username, password=password, email=username)
    return user
