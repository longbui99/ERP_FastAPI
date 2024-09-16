import os
import hashlib

from app.base.exceptions import ServerMisConfigured

def hashkey(key: str) -> str:
    if 'PASSWORD_HASH' not in os.environ:
        raise ServerMisConfigured("PASSWORD_HASH not found")
    key = os.environ['PASSWORD_HASH'] + "-" + key
    return  hashlib.sha256(key.encode('utf-8')).hexdigest()