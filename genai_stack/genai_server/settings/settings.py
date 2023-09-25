from pydantic import BaseSettings
from configparser import ConfigParser

genai_stack_config = ConfigParser()


class Settings(BaseSettings):
    CONNECTION_STRING: str = genai_stack_config.get("sqlite", "connection_string")
    DATABASE_NAME: str = genai_stack_config.get("sqlite", "db_name")

    class Config:
        pass


settings = Settings()
