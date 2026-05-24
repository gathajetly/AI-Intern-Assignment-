# backend/app/models/extraction.py
from sqlalchemy import Column, String, Text, JSON, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
import uuid
from app.core.database import Base

class Extraction(Base):
    __tablename__ = "extractions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    document_id = Column(String, ForeignKey("documents.id"), nullable=False)
    raw_text = Column(Text, nullable=False)
    structured_data = Column(JSON, nullable=False)
    extracted_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    document = relationship("Document", backref="extraction")