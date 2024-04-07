from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# Shared properties
class UserReportBase(BaseModel):
    reason: Optional[str] = None

# Properties to receive on UserReport creation
class UserReportCreate(UserReportBase):
    reporter_id: int
    reported_id: int
    reason: str

# Properties to receive on UserReport update
class UserReportUpdate(UserReportBase):
    pass

# Properties shared by models stored in DB
class UserReportInDBBase(UserReportBase):
    id: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True

# Properties to return to client
class UserReport(UserReportInDBBase):
    pass

# Properties stored in DB
class UserReportInDB(UserReportInDBBase):
    pass
