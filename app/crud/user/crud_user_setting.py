from typing import Any, Dict, Optional, Union
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user_setting import UserSettings  # Ensure you have this model defined
from app.schemas.user_setting import UserSettingsCreate, UserSettingsUpdate  # Define these schemas

class CRUDUserSettings(CRUDBase[UserSettings, UserSettingsCreate, UserSettingsUpdate]):
    def create_with_user(
        self, db: Session, *, obj_in: UserSettingsCreate, user_id: int
    ) -> UserSettings:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)  # Assumes UserSettings model has a user_id field
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_user_id(
        self, db: Session, *, user_id: int
    ) -> Optional[UserSettings]:
        return (
            db.query(self.model)
            .filter(UserSettings.user_id == user_id)
            .first()
        )

    def update_with_user(
        self, db: Session, *, db_obj: UserSettings, obj_in: Union[UserSettingsUpdate, Dict[str, Any]]
    ) -> UserSettings:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

user_settings = CRUDUserSettings(UserSettings)
