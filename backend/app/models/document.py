# backend/app/models/document.py
from sqlalchemy import Column, String, DateTime
from datetime import datetime, timezone
import uuid
from app.core.database import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    status = Column(String, default="uploaded") # Can be 'uploaded', 'extracted', 'drafted'
    uploaded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))