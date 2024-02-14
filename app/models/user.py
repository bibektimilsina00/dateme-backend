from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, DECIMAL, Enum, Text, create_engine
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    auth_provider = Column(String)
    country_id = Column(Integer, ForeignKey('country.id'))
    full_name = Column(String)
    gender = Column(String)
    date_of_birth = Column(DateTime)
    location = Column(String)
    profile_status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    country = relationship("Country", back_populates="users")
    images = relationship("UserImage", back_populates="user")
    interests = relationship("UserInterest", back_populates="user")
    preferences = relationship("UserPreference", back_populates="user")
    sent_messages = relationship("Message", back_populates="sender")
    notifications = relationship("Notification", back_populates="user")
    locations = relationship("UserLocation", back_populates="user")
    activity_logs = relationship("ActivityLog", back_populates="user")