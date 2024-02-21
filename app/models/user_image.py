from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, DECIMAL, Enum, Text, create_engine

from app.db.base_class import Base
from sqlalchemy.orm import relationship


class UserImage(Base):
    image_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    image_url = Column(String)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", backref="images")