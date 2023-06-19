import os

from pydantic import BaseSettings, BaseModel

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_PATH = os.path.dirname(BASE_PATH)


class Settings(BaseSettings):
    # App settings
    app_name: str = "to-telegram"
    debug: bool = False

    class Config:
        env_file = os.path.join(ROOT_PATH, ".env")
        env_file_encoding = "utf-8"
        env_nested_delimiter = '_'


settings = Settings()
