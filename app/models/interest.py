from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, DECIMAL, Enum, Text, create_engine

from app.db.base_class import Base
from sqlalchemy.orm import relationship

class Interest(Base):
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    interest_name = Column(String)
    
    user_interests = relationship("UserInterest", back_populates="interest")