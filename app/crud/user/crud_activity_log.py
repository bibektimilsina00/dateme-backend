from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app.crud.base import CRUDBase

from app.models.activity_log import ActivityLog   
from app.schemas.activity_log import ActivityLogCreate, ActivityLogUpdate  

class CRUDActivityLog(CRUDBase[ActivityLog, ActivityLogCreate, ActivityLogUpdate]):
    def create_with_user(
        self, db: Session, *, obj_in: ActivityLogCreate, user_id: int
    ) -> ActivityLog:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_user_id(
        self, db: Session, *, user_id: int
    ) -> Optional[ActivityLog]:
        return (
            db.query(self.model)
            .filter(ActivityLog.user_id == user_id)
            .all()
        )

activity_log = CRUDActivityLog(ActivityLog)
