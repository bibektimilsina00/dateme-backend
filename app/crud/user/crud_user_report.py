from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app.crud.base import CRUDBase

from app.models.user_report import UserReport  # Ensure you have this model
from app.schemas.user_report import UserReportCreate, UserReportUpdate  # Import the schemas

class CRUDUserReport(CRUDBase[UserReport, UserReportCreate, UserReportUpdate]):
    def create(
        self, db: Session, *, obj_in: UserReportCreate
    ) -> UserReport:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_id(
        self, db: Session, *, id: int
    ) -> Optional[UserReport]:
        return db.query(self.model).filter(UserReport.id == id).first()

user_report = CRUDUserReport(UserReport)
