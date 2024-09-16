from typing import Annotated, List

from fastapi import Form, Depends, Body, HTTPException, status
from fastapi.responses import Response
from fastapi.security import OAuth2PasswordBearer
from fastapi.encoders import jsonable_encoder

from app import app
from app.models.login import LoginCredential
from app.models.users import User, _User
from app.utils.jwt import encode_json_to_jwt, decode_jwt_to_json
from app.utils.auth import hashkey

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def _login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    user = await _User.get(login=username)
    if not user:
        return Response("Username not found", 406)
    if user.password != hashkey(password):
        return Response("Password not found", 406)
    return user

async def authorized_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = _User(**decode_jwt_to_json(token))
    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

@app.post('/login')
def get_login(user: Annotated[_User, Depends(_login)]):
    if not isinstance(user, _User):
        return user
    return {"access_token": encode_json_to_jwt(jsonable_encoder(user)), "token_type": "bearer"}

@app.post('/sign-up', response_model=User)
async def signup(username: Annotated[str, Body()], password: Annotated[str, Body()]):
    user = await _User.exists(login=username)
    if user:
        return Response("The username is already taken", 406)
    user = await _User.create(login=username, password=hashkey(password), email=username)
    return user

@app.delete('/user/delete')
async def delete(user: Annotated[_User, Depends(authorized_user)]) -> bool:
    await user.get().delete()
    return True
