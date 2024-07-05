from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String,DateTime,DECIMAL, func,Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base



class UserLocation(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


