from pydantic import BaseSettings, validator
from typing import Optional, Dict, Any
from sqlalchemy.sql.schema import MetaData

from genai_stack.genai_server.schemas import BaseSchema, StackSessionSchema
from genai_stack.genai_server.settings.config import path, stack_config, server_config
from genai_stack.genai_store.sql_store import SQLStore
from genai_stack.genai_server.services.session_service import SessionService
from genai_stack.genai_server.models.session_models import StackSessionResponseModel


class Settings(BaseSettings):
    RUNTIME_PATH: str = path
    DATABASE_NAME: str = server_config.get("database", "database_name")
    DATABASE_DRIVER: str = server_config.get("database", "database_driver")
    DATABASE_URI: Optional[str] = None
    STACK_CONFIG: dict = stack_config
    META_DATA: MetaData = BaseSchema.metadata
    TABLE_NAME: str = StackSessionSchema.__tablename__
    STORE:Optional[SQLStore] = None 
    DEFAULT_SESSION:Optional[StackSessionResponseModel] = None

    @validator("DATABASE_URI", pre=True)
    def assemble_database_uri(cls, v, values: Dict[str, Any]) -> str:
        return values["DATABASE_DRIVER"] + ":///" + values["RUNTIME_PATH"] + "/" + values["DATABASE_NAME"]
    
    @validator("STORE", pre=True)
    def initialize_store(cls, v, values:Dict[str, Any]) -> SQLStore:
        return SQLStore(url=values["DATABASE_URI"], meta_data=values["META_DATA"], table_name=values['TABLE_NAME'])
    
    @validator("DEFAULT_SESSION", pre=True)
    def create_default_session(cls, v, values:Dict[str, Any]) -> StackSessionResponseModel:
        session = SessionService(store=values['STORE'])
        return session.create_session()

    class Config:
        case_sensitive = True
        # env_file = ".env"


settings = Settings()
