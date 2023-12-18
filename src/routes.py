from fastapi import APIRouter

from .user import routes as user_routes
from .invitation import routes as invitation_routes
from .meet import routes as meet_routes


def get_apps_router():
    router = APIRouter()
    router.include_router(user_routes.get_context_router())
    router.include_router(invitation_routes.get_context_router())
    router.include_router(meet_routes.get_context_router())
    return router
