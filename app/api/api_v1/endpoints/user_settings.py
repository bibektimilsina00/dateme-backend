from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models
from app.crud.user.crud_user_setting import user_settings as crud_user_settings  # This should be your CRUD class for UserSettings
from app.schemas import user_setting as user_settings_schema
from app.api import deps

router = APIRouter()

@router.get("/user_settings/", response_model=user_settings_schema.UserSettings)
def read_user_settings(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve user settings for the current user.
    """
    user_settings = crud_user_settings.get_by_user_id(db=db, user_id=current_user.id)
    if not user_settings:
        raise HTTPException(status_code=404, detail="UserSettings not found")
    return user_settings

@router.post("/user_settings/", response_model=user_settings_schema.UserSettings)
def create_user_settings(
    *,
    db: Session = Depends(deps.get_db),
    settings_in: user_settings_schema.UserSettingsCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create or update user settings for the current user.
    """
    user_settings = crud_user_settings.get_by_user_id(db=db, user_id=current_user.id)
    if user_settings:
        raise HTTPException(status_code=400, detail="UserSettings already exist for the current user")
    user_settings = crud_user_settings.create_with_user(db=db, obj_in=settings_in, user_id=current_user.id)
    return user_settings

@router.put("/user_settings/", response_model=user_settings_schema.UserSettings)
def update_user_settings(
    *,
    db: Session = Depends(deps.get_db),
    settings_in: user_settings_schema.UserSettingsUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update user settings for the current user.
    """
    user_settings = crud_user_settings.get_by_user_id(db=db, user_id=current_user.id)
    if not user_settings:
        raise HTTPException(status_code=404, detail="UserSettings not found")
    user_settings = crud_user_settings.update(db=db, db_obj=user_settings, obj_in=settings_in)
    return user_settings
