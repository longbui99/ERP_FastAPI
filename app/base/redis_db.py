import redis

from app.base.config import config
from app.utils.sql_db import load_modules
from app.base.exceptions import InternalServerError


def init_redis_connection() -> None:
    r = redis.Redis(host=config['database']['redis_host'], port=int(config['database']['redis_port']))
    r.ping()
    return r

class RedisConnectionPoll():
    def __init__(self) -> None:
        self.conn = None

    def _connection_sanity_check(self):
        if not self.conn:
            raise InternalServerError("Redis Connection Is terminated")

    def set_connection(self, r: redis.Redis) -> None:
        self.conn = r
    
    def get(self, key) -> dict:
        self._connection_sanity_check()
        return self.conn.get(key)
    
    def set(self, key, value) -> None:
        self._connection_sanity_check()
        return self.conn.set(key, value)
    
rconn = RedisConnectionPoll()