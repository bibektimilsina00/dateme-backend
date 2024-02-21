from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String,DateTime, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base









class Notification(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)  # Optional: A short title for the notification
    content = Column(String, nullable=False)  # The content or message of the notification
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # ForeignKey to the User model
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Timestamp for when the notification was created
    
    # Relationship to User
    user = relationship("User", backref="notifications")