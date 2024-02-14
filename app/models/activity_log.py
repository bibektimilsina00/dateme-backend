from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String,DateTime,Text, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base





class ActivityLog(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    activity_type = Column(String, nullable=False)  # Example: 'login', 'swipe', etc.
    details = Column(Text)  # Additional details about the activity
    created_at = Column(DateTime, default=func.now(), nullable=False)

    # Relationship to User
    user = relationship("User", back_populates="activity_logs")
