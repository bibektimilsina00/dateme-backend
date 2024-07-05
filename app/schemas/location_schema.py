from typing import Optional

from pydantic import BaseModel
from datetime import datetime


# Shared properties
class UserLocation(BaseModel):
    name: Optional[str]
    latitude: float
    longitude: float


# Properties to receive on CustomLocation creation
class CustomLocationCreate(UserLocation):
    pass


# Properties to receive on CustomLocation update
class CustomLocationUpdate(UserLocation):
    pass


# Properties shared by models stored in DB
class UserLocationInDBBase(UserLocation):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Properties to return to client
class CustomLocation(UserLocationInDBBase):
    pass


# Properties properties stored in DB
class CustomLocationInDB(UserLocationInDBBase):
    pass
