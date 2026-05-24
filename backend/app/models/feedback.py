# backend/app/models/feedback.py
from sqlalchemy import Column, String, Text, DateTime
from datetime import datetime, timezone
import uuid
from app.core.database import Base

class Feedback(Base):
    __tablename__ = "feedback_rules"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    draft_id = Column(String, nullable=False, index=True)
    original_text = Column(Text, nullable=False)
    edited_text = Column(Text, nullable=False)
    learned_rule = Column(Text, nullable=False)
    is_active = Column(String, default="true") 
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))