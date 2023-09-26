import enum
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
    data: dict


class ETLJobResponseType(BaseModel):
    pass

