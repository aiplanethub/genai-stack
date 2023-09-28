import enum
from sqlalchemy import Column, Integer, JSON, ForeignKey, Enum

from genai_stack.genai_server.schemas.base_schemas import TimeStampedSchema


class ETLJobStatus(enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"


class ETLJob(TimeStampedSchema):
    """
    SQL Schema for ETL Jobs.
    """

    __tablename__ = "etl_jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    stack_session = Column(
        Integer, ForeignKey("stack_sessions.id", ondelete="CASCADE"), nullable=False
    )
    meta_data = Column(JSON, nullable=True)
    status = Column(Enum(ETLJobStatus), default=ETLJobStatus.PENDING)
    data = Column(JSON, nullable=True)
