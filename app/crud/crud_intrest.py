
from app.crud.base import CRUDBase
from app.models.interest import Interest
from app.schemas.user_interests import InterestCreate, InterestUpdate


class CRUDIInterest(CRUDBase[Interest, InterestCreate, InterestUpdate]):
    pass


interest = CRUDIInterest(Interest)
