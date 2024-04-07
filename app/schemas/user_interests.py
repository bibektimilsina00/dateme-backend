from typing import Optional

from pydantic import ConfigDict, BaseModel


# Shared properties
class InterestBase(BaseModel):
    title: Optional[str] = None
    image_url: Optional[str] = None


# Properties to receive on Interest creation
class InterestCreate(InterestBase):
    pass


# Properties to receive on Interest update
class InterestUpdate(InterestBase):
    pass


# Properties shared by models stored in DB
class InterestInDBBase(InterestBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class Interest(InterestInDBBase):
    pass


# Properties properties stored in DB
class InterestInDB(InterestInDBBase):
    pass
