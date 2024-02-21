from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String,DateTime,DECIMAL, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base



class UserLocation(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    latitude = Column(DECIMAL(9, 6))
    longitude = Column(DECIMAL(9, 6))
    timestamp = Column(DateTime, default=func.now(), nullable=False)
    
    user = relationship("User", backref="locations")

