from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, JSON,func
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    auth_provider = Column(String, default='local')
    country_id = Column(Integer, ForeignKey('country.id'))
    country = relationship("Country", backref="users")
    gender = Column(String)
    date_of_birth = Column(DateTime)
    location = Column(String)
    profile_status = Column(String, default='Active')
    bio = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    phone_number = Column(String)
    profession = Column(String)
    profile_pic_url = Column(String)
    address = Column(String)
    profile_image_urls = Column(JSON)
