from typing import List
from glob import glob
from os import environ, getcwd
from importlib import import_module
from inspect import isclass

from tortoise.models import Model

from app.base.config import config


def get_database_admin_password() -> str:
    master_password = config['server'].get('master_password')
    if 'DATABASE_MASTER_PASSWORD' in environ:
        master_password = environ['DATABASE_MASTER_PASSWORD']
    return master_password

def load_modules(app: str) -> List[str]:
    execution_path = getcwd()
    modules = config['server'].get('modules')
    response = []
    for module in modules.split(','):
        paths = glob(f"{execution_path.strip().rstrip('/')}/{module}")
        for fpath in paths:
            fpaths = fpath[len(execution_path)+1:-3].split('/')
            name = f"{app}.{'.'.join(fpaths)}"
            response.append(name)
    final_response = []
    travel_modules = dict()
    for models_path in response:
        module = import_module(models_path)
        possible_models = [getattr(module, attr_name) for attr_name in dir(module)]
        for attr in possible_models:
            if isclass(attr) and issubclass(attr, Model) and attr not in travel_modules and not attr._meta.abstract:
                if attr._meta.app and attr._meta.app != app:
                    continue
                final_response.append(models_path)
                travel_modules[attr] = 1
                continue
    return final_response