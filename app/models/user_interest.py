
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, DECIMAL, Enum, Text, create_engine

from app.db.base_class import Base
from sqlalchemy.orm import relationship

class UserInterest(Base):
    
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    interest_id = Column(Integer, ForeignKey('interest.id'), primary_key=True)
    
    user = relationship("User", backref="interests")
    interest = relationship("Interest", backref="user_interests")