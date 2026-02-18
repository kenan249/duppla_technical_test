import uuid
from sqlalchemy import Column, String, Numeric, DateTime, Integer, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Document(Base):
    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True)
    document_type = Column(String)
    amount = Column(Numeric(12, 2))
    status = Column(String)
    created_at = Column(DateTime(timezone=True))
    metadata = Column(JSONB)


class Job(Base):
    __tablename__ = "jobs"

    id = Column(UUID(as_uuid=True), primary_key=True)
    status = Column(String)
    total = Column(Integer)
    processed = Column(Integer)
    requested_ids = Column(JSONB)
    error = Column(Text)
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True))

