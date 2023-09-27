from pydantic import BaseSettings, validator
from typing import Optional, Dict, Any
from sqlalchemy.sql.schema import MetaData

from genai_stack.genai_server.schemas import BaseSchema, StackSessionSchema
from genai_stack.genai_server.settings.config import path, stack_config, server_config

class Settings(BaseSettings):
    RUNTIME_PATH:str = path
    DATABASE_NAME:str = server_config.get("database","database_name")
    DATABASE_DRIVER:str = server_config.get("database","database_driver")
    DATABASE_URI:Optional[str] = None
    STACK_CONFIG:dict = stack_config
    META_DATA:MetaData = BaseSchema.metadata
    TABLE_NAME:str = StackSessionSchema.__tablename__

    @validator("DATABASE_URI", pre=True)
    def assemble_database_uri(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v
        return values["DATABASE_DRIVER"] + ":///" + values["RUNTIME_PATH"] + "/" + values["DATABASE_NAME"]
      
    class Config:
        case_sensitive = True
        # env_file = ".env"


settings = Settings()
