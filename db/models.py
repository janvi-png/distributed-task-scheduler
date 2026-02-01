from sqlalchemy import Column, Integer, String, DateTime, Enum
from datetime import datetime
import enum
from db.database import Base

class JobStatus(str, enum.Enum):
    pending = "PENDING"
    running = "RUNNING"
    done = "DONE"
    failed = "FAILED"

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    task_type = Column(String, index=True)
    payload = Column(String)
    status = Column(Enum(JobStatus), index=True)
    attempts = Column(Integer, default=0)
    updated_at = Column(DateTime, default=datetime.utcnow)
