from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String,DateTime, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base







class Chat(Base):
    
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # Relationship to Message
    messages = relationship("Message", back_populates="chat")

    # If you want to track participants of the chat, you might need a many-to-many relationship
    # participants = relationship("User", secondary="chat_participants")