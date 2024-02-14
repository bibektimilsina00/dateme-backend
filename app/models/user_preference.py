from sqlalchemy import Column, ForeignKey, Integer, String,Text

from app.db.base_class import Base
from sqlalchemy.orm import relationship

class UserPreference(Base):
    preference_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    preferred_gender = Column(String)
    age_range = Column(String)
    location_radius = Column(Integer)
    looking_for = Column(Text)
    
    user = relationship("User", back_populates="preferences")