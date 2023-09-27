import enum
from typing import Any, Dict
from pydantic import BaseModel


class StatusEnum(enum.Enum):
    Pending = "Pending"
    Processing = "Processing"
    Completed = "Completed"


class BaseETLJobType(BaseModel):
    uuid: str
    session_id: int
    status: StatusEnum
    metadata: dict


class ETLJobRequestType(BaseModel):
    __root__: Dict[str, Any]


class ETLJobResponseType(BaseModel):
    pass
