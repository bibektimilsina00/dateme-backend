
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, DECIMAL, Enum, Text, create_engine

from app.db.base_class import Base
from sqlalchemy.orm import relationship




class UserSettings(Base):
    
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    enable_notifications = Column(Boolean, default=False)
    use_biometric_auth = Column(Boolean, default=False)
    biometric_auth_type = Column(String)
    enable_location = Column(Boolean, default=False)

    user = relationship("User", backref="settings")