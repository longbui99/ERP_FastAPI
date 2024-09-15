from os import environ

from app.base.config import config

def get_database_admin_password():
    master_password = config['server'].get('master_password')
    if 'DATABASE_MASTER_PASSWORD' in environ:
        master_password = environ['DATABASE_MASTER_PASSWORD']
    return master_password