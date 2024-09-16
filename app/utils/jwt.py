from os import environ
import jwt


from app.models.users import User, _User
from app.base.exceptions import ServerMisConfigured


def _get_os_key():
    key = environ.get("APISERVER_KEY")
    if key is None:
        raise ServerMisConfigured("LOGIN SECURITY KEY NOT FOUND")
    return key

def encode_json_to_jwt(user: dict) -> str:
    key = _get_os_key()
    encoded_jwt = jwt.encode(user, key, algorithms="HS256")
    return encoded_jwt

def decode_jwt_to_json(jwt_key: str) -> dict:
    key = _get_os_key()
    user = jwt.decode(jwt_key, key, algorithms="HS256")
    return user
