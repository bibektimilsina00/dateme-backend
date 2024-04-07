from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import user_interests as schemas
from app.api import deps
from app.crud.crud_intrest import interest as crud_intrest

router = APIRouter()


@router.get("/", response_model=List[schemas.Interest])
def read_items(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve Interest.
    """
    country =crud_intrest.get_multi(db, skip=skip, limit=limit)
    
    return country



