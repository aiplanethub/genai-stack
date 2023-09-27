import enum
from sqlalchemy import Column, Integer, JSON, ForeignKey, UUID, Enum

from genai_stack.genai_server.schemas.base_schemas import TimeStampedSchema


class JobStatus(enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"


class ETLJob(TimeStampedSchema):
    """
    SQL Schema for ETL Jobs.
    """

    __tablename__ = "etl_jobs"

    id = Column(UUID, primary_key=True, autoincrement=True)
    stack_session = Column(
        Integer, ForeignKey("stack_sessions.id", ondelete="CASCADE"), nullable=False, primary_key=True
    )
    metadata = Column(JSON, nullable=True)
    status = Column(Enum(JobStatus), default=JobStatus.PENDING)
    data = Column(JSON, nullable=True)
