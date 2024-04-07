from sqlalchemy import Column,  Integer, String

from app.db.base_class import Base
from sqlalchemy.orm import relationship

class Interest(Base):  
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    image_url= Column(String)
    