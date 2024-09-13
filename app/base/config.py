from typing import Any
from configparser import RawConfigParser

class ConfigManager:
    def __init__(self, fname=None) -> None:
        self.fname = fname
        self.config = {}

    def __getitem__(self, key: str) -> None:
        return self.config[key]
    
    def get(self, key: str, default: str | None = None) -> Any:
        return self.config.get(key, default)

    def parse_config(self, fname=None) -> None:
        file_path = fname
        if not file_path:
            file_path = self.fname
        if not file_path:
            return
        config = RawConfigParser()
        config.read([fname])
        self.config = dict(config.items('options'))


config = ConfigManager()