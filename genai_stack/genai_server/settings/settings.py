from pydantic import BaseSettings, validator
from typing import Optional, Dict, Any

from genai_stack.genai_server.settings.config import path, stack_config

class Settings(BaseSettings):
    RUNTIME_PATH:str = path
    DATABASE_NAME:str = "db"
    DATABASE_DRIVER:str = "sqlite"
    DATABASE_URI:Optional[str] = None
    STACK_CONFIG:dict = stack_config

    @validator('DATABASE_URI', pre=True)
    def create_database_uri(cls, values: Dict[str, Any]):
            return f"{values.get('DATABASE_DRIVER')}:////{values.get('RUNTIME_PATH')}/{values.get('DATABASE_NAME')}"

    class Config:
        case_sensitive = True
        # env_file = ".env"


settings = Settings()
