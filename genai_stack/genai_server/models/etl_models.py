import enum
from typing import Any, Dict, Optional
from pydantic import BaseModel

from genai_stack.genai_server.schemas import ETLJobStatus


class BaseETLJobModel(BaseModel):
    id: int
    session_id: int
    status: ETLJobStatus
    metadata: Optional[dict]


class ETLJobRequestType(BaseModel):
    __root__: Dict[str, Any]


class ETLJobResponseType(BaseETLJobModel):
    pass
