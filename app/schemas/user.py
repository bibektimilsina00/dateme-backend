from datetime import datetime
from typing import Optional,List

from pydantic import ConfigDict, BaseModel, EmailStr

from app.schemas.country import Country
from app.schemas.user_location import UserLocationCreate

# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None
    auth_provider: Optional[str] = None
    phone_number: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    
    profile_status: Optional[str] = None
    bio: Optional[str] = None
    profession: Optional[str] = None 
    profile_pic_url: Optional[str] = None
    address : Optional[str] = None
    profile_image_urls :Optional[List[str]] = None 

# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str
    full_name: str
    country_id: int
    phone_number:str
    gender:str
    date_of_birth:str
    profile_status:str='Active'
    bio:str
    profession:str
    profile_pic_url:str
    address:str
    profile_image_urls:List[str]
    location: Optional[UserLocationCreate] = None
    
# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDBBase(UserBase):
    id: Optional[int] = None
    creaded_at: Optional[ datetime] = None
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)
    
# Additional properties to return via API
class User(UserInDBBase):
    country: Optional[Country] = None
    
    pass

# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
