from typing import Optional

from pydantic import ConfigDict, BaseModel


# Shared properties
class CountryBase(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None


# Properties to receive on country creation
class CountryCreate(CountryBase):
    pass


# Properties to receive on country update
class CountryUpdate(CountryBase):
    pass


# Properties shared by models stored in DB
class CountryInDBBase(CountryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class Country(CountryInDBBase):
    pass


# Properties properties stored in DB
class CountryInDB(CountryInDBBase):
    pass
