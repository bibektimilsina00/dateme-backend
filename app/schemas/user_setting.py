from typing import Optional
from pydantic import BaseModel

# Shared properties
class UserSettingsBase(BaseModel):
    enable_notifications: Optional[bool] = None
    use_biometric_auth: Optional[bool] = None
    biometric_auth_type: Optional[str] = None

# Properties to receive on user settings creation
class UserSettingsCreate(UserSettingsBase):
    enable_notifications: bool   
    use_biometric_auth: bool   

# Properties to receive on user settings update
class UserSettingsUpdate(UserSettingsBase):
    pass

# Properties shared by models stored in DB
class UserSettingsInDBBase(UserSettingsBase):
    id: int  
    user_id: int  

    class Config:
        from_attributes = True

# Properties to return to client
class UserSettings(UserSettingsInDBBase):
    pass

# Properties properties stored in DB
class UserSettingsInDB(UserSettingsInDBBase):
    pass
