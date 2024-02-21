from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models
from app.crud.user.crud_user_report import user_report as crud_user_report  # Adjust this to your CRUD class path
from app.schemas.user_report import UserReportCreate, UserReport
from app.api import deps

router = APIRouter()

@router.post("/user_reports/", response_model=UserReport)
def create_user_report(
    *,
    db: Session = Depends(deps.get_db),
    user_report_in: UserReportCreate,
) -> Any:
    """
    Create a new user report.
    """
    user_report = crud_user_report.create(db=db, obj_in=user_report_in)
    return user_report

@router.get("/user_reports/{id}", response_model=UserReport)
def read_user_report(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get user report by ID.
    """
    user_report = crud_user_report.get_by_id(db=db, id=id)
    if not user_report:
        raise HTTPException(status_code=404, detail="UserReport not found")
    return user_report
