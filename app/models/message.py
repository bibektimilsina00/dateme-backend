from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String,DateTime, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Message(Base):
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey('chat.id'))
    content = Column(String)
    sent_at = Column(DateTime(timezone=True), server_default=func.now())

    user_id = Column(Integer, ForeignKey('user.id'))
    sender = relationship("User", backref="sent_messages")
    # Relationship to Chat
    chat = relationship("Chat", backref="messages")