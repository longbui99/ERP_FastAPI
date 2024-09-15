from os import environ
import jwt

from fastapi.encoders import jsonable_encoder

from app.models.login import LoginCredential
from app.base.exceptions import ServerMisConfigured


def _get_os_key():
    key = environ.get("APISERVER_KEY")
    if key is None:
        raise ServerMisConfigured("LOGIN SECURITY KEY NOT FOUND")
    return key

def encode_login_to_jwt(login: LoginCredential) -> str:
    key = _get_os_key()
    encoded_jwt = jwt.encode(jsonable_encoder(login), key, algorithm="HS256")
    return encoded_jwt

def decode_jwt_to_login(jwt: str) -> LoginCredential:
    key = _get_os_key()
    login = LoginCredential(**jwt.decode(jwt, key, algorithm="HS256"))
    return login
