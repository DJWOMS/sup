from fastapi import APIRouter
from .user import routes as user_routes


def get_apps_router():
    router = APIRouter()
    router.include_router(user_routes.get_context_router())
    return router
