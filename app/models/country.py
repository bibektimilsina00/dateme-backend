from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, DECIMAL, Enum, Text, create_engine

from app.db.base_class import Base
from sqlalchemy.orm import relationship


if TYPE_CHECKING:
    from .user import User

class Country(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    country_name = Column(String)
    country_code = Column(String)
    
    users = relationship("User", back_populates="country")