from pydantic import BaseSettings
from genai_stack.genai_platform.settings.config import genai_stack_config

class Settings(BaseSettings):
    CONNECTION_STRING:str = genai_stack_config.get("sqlite", "connection_string")
    DATABASE_NAME:str = genai_stack_config.get("sqlite","db_name")

    class Config:
       # env_file = ".env"
       pass

settings = Settings()