from sqlalchemy.orm import Session

from app.crud.user import crud_user
from app.schemas import user as schemas
from app.core.config import settings
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    user = crud_user.user.get_by_email(db, email=settings.FIRST_SUPERUSER)

    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            full_name="Superuser",
            country_id=1,
            phone_number='123456789',
            gender="Male",
            date_of_birth="1990-01-01",
            bio="I am a superuser",
            profession="Software Engineer",
            profile_pic_url="https://example.com/profile_pic",
            address="123, Main Street",
            profile_image_urls=["https://example.com/image1", "https://example.com/image2"]
        )
        user = crud_user.user.create(db, obj_in=user_in)  # noqa: F841
