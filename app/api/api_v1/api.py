from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils,country,user_settings,activity_log,user_report,interest

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(country.router, prefix="/country", tags=["country"])
api_router.include_router(interest.router, prefix="/interest", tags=["Interest"])
api_router.include_router( user_settings.router, prefix="/user-settings", tags=["user-settings"])
api_router.include_router( activity_log.router, prefix="/activity-log", tags=["activity-log"])
api_router.include_router( user_report.router, prefix="/user-report", tags=["user-report"])
