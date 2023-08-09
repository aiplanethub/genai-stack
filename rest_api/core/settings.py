from typing import Any, Dict, List, Optional, Union

from pydantic import BaseSettings, validator
from .config import server_config


class Settings(BaseSettings):
    PROJECT_NAME: str = "LLM Stack Server"
    DEBUG_MODE = bool(int(server_config.get("app", "debug_mode", fallback="0")))
    BACKEND_CORS_ORIGINS: List[str] = list(
        map(lambda s: s.strip(), server_config.get("cors", "whitelist").split(","))
    )

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # SQLite
    DATABASE_URL = server_config.get("database", "url")

    class Config:
        case_sensitive = True
        # env_file = ".env"


settings = Settings()
