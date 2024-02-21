from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import country as schemas
from app.api import deps
from app.crud import crud_country

router = APIRouter()


@router.get("/", response_model=List[schemas.Country])
def read_items(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve items.
    """
   
    country =crud_country.country.get_multi (db, skip=skip, limit=limit)
    return country


 


 

 

 


 



