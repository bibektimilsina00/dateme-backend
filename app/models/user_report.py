from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String,DateTime,Text, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base



class UserReport(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    reporter_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    reported_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    reason = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())

    reporter = relationship("User", foreign_keys=[reporter_id], backref="reported_by_user")
    reported = relationship("User", foreign_keys=[reported_id], backref="reports_against_user")
