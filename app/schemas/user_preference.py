from typing import Optional
from pydantic import BaseModel

# Shared properties
class UserPreferenceBase(BaseModel):
    preferred_gender: Optional[str] = None
    age_range: Optional[str] = None
    location_radius: Optional[int] = None
    looking_for: Optional[str] = None

# Properties to receive on UserPreference creation
class UserPreferenceCreate(UserPreferenceBase):
    preferred_gender: str
    age_range: str
    location_radius: int
    looking_for: str

# Properties to receive on UserPreference update
class UserPreferenceUpdate(UserPreferenceBase):
    pass

# Properties shared by models stored in DB
class UserPreferenceInDBBase(UserPreferenceBase):
    preference_id: int
    user_id: int

    class Config:
        orm_mode = True

# Properties to return to client
class UserPreference(UserPreferenceInDBBase):
    pass

# Properties stored in DB
class UserPreferenceInDB(UserPreferenceInDBBase):
    pass
