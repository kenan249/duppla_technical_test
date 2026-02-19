import uuid
from sqlalchemy import Column, String, Numeric, DateTime, Integer, Text, Enum
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import DeclarativeBase

from app.domain.enums.document_status import DocumentStatus
from app.domain.enums.job_status import JobStatus


class Base(DeclarativeBase):
    pass


class Document(Base):
    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True)
    document_type = Column(String)
    amount = Column(Numeric(12, 2))
    status = Column(Enum(DocumentStatus, name="document_status"))
    created_at = Column(DateTime(timezone=True))
    metadata_dic = Column(JSONB)


class Job(Base):
    __tablename__ = "jobs"

    id = Column(UUID(as_uuid=True), primary_key=True)
    status = Column(Enum(JobStatus, name="job_status"))
    total = Column(Integer)
    processed = Column(Integer)
    requested_ids = Column(JSONB)
    error = Column(Text)
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True))

