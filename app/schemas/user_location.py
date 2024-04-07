from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# Shared properties
class UserLocationBase(BaseModel):
    latitude: Optional[float] = None
    longitude: Optional[float] = None

# Properties to receive on UserLocation creation
class UserLocationCreate(UserLocationBase):
    latitude: float
    longitude: float

# Properties to receive on UserLocation update
class UserLocationUpdate(UserLocationBase):
    pass

# Properties shared by models stored in DB
class UserLocationInDBBase(UserLocationBase):
    id: Optional[int] = None
    user_id: int
    timestamp: datetime

    class Config:
        from_attributes = True

# Properties to return to client
class UserLocation(UserLocationInDBBase):
    pass

# Properties stored in DB
class UserLocationInDB(UserLocationInDBBase):
    pass
