from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# Shared properties
class ActivityLogBase(BaseModel):
    activity_type: Optional[str] = None
    details: Optional[str] = None

# Properties to receive on ActivityLog creation
class ActivityLogCreate(ActivityLogBase):
    activity_type: str
    details: str

# Properties to receive on ActivityLog update
class ActivityLogUpdate(ActivityLogBase):
    pass

# Properties shared by models stored in DB
class ActivityLogInDBBase(ActivityLogBase):
    id: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True

# Properties to return to client
class ActivityLog(ActivityLogInDBBase):
    pass

# Properties stored in DB
class ActivityLogInDB(ActivityLogInDBBase):
    pass
