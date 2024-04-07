from datetime import datetime
from typing import Any, List, Optional

from fastapi import APIRouter, Body, Depends, File, Form, HTTPException, UploadFile
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import models
from app.schemas import user as schemas
from app.crud.user.crud_user import user as crud_user

from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email
from app.utilities.file_utils import save_uploaded_image

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    users = crud_user.get_multi(db, skip=skip, limit=limit)
    return users

@router.get('/recomended_users/', response_model=List[schemas.User])
def get_recomended_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 10,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve users.
    """
    # users = crud_user.get_recomended_users(db, current_user)
    users = crud_user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/upload_images/")
def upload_images(
    db: Session = Depends(deps.get_db),
    images: List[UploadFile] = File(...),
    profile_picture: UploadFile = None,
) -> Any: 
    UPLOAD_FOLDER='static/uploaded_images/'
    user_images_path = []
    for image in images:
        try:
            profile_picture_path = save_uploaded_image(profile_picture, UPLOAD_FOLDER)
            file_path = save_uploaded_image(image, UPLOAD_FOLDER)
            user_images_path.append(file_path)
        except Exception as e:
            print(f"Error saving image {image.filename}: {e}")
            return HTTPException(status_code=400, detail=f"Error saving image {image.filename}: {e}")
    return {"images": user_images_path, "profile_picture": profile_picture_path}
        


@router.post("/", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
) -> Any:
    
    if crud_user.get_by_email(db, email=user_in.email):
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user = crud_user.create(db=db, obj_in=user_in)
    print(user)
    # Send confirmation email if enabled
    if settings.EMAILS_ENABLED and user.email:
        send_new_account_email(
            email_to=user.email, username=user.email, password=user_in   
        )

    return user


@router.put("/me", response_model=schemas.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    user = crud_user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.post("/open", response_model=schemas.User)
def create_user_open(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    full_name: str = Body(None),
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    user = crud_user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_in = schemas.UserCreate(password=password, email=email, full_name=full_name)
    user = crud_user.create(db, obj_in=user_in)
    return user


@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = crud_user.get(db, id=user_id)
    if user == current_user:
        return user
    if not crud_user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user


@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a user.
    """
    user = crud_user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = crud_user.update(db, db_obj=user, obj_in=user_in)
    return user
