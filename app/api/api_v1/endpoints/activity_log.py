from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models
from app.crud.user.crud_activity_log import activity_log as crud_activity_log  # This should point to your CRUD class for ActivityLog
from app.schemas.activity_log import ActivityLogCreate, ActivityLog, ActivityLogUpdate
from app.api import deps

router = APIRouter()

@router.get("/activity_logs/{user_id}", response_model=List[ActivityLog])
def read_activity_logs(
    user_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve activity logs for a specific user.
    """
    activity_logs = crud_activity_log.get_by_user_id(db=db, user_id=user_id)
    return activity_logs

@router.post("/activity_logs/", response_model=ActivityLog)
def create_activity_log(
    *,
    db: Session = Depends(deps.get_db),
    activity_log_in: ActivityLogCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create a new activity log.
    """
    activity_log = crud_activity_log.create_with_user(db=db, obj_in=activity_log_in, user_id=current_user.id)
    return activity_log
