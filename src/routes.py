from fastapi import APIRouter

from .email import routes as email_controller
from .user import routes as user_routes
from .invitation import routes as invitation_routes
from .meet import routes as meet_routes
from .login import routes as login_controller
from .permission import routes as permission_controller
from .role import routes as role_controller


def get_apps_router():
    router = APIRouter()
    router.include_router(user_routes.get_context_router())
    router.include_router(invitation_routes.get_context_router())
    router.include_router(meet_routes.get_context_router())
    router.include_router(email_controller.get_context_router())
    router.include_router(login_controller.get_context_router())
    router.include_router(permission_controller.get_context_router())
    router.include_router(role_controller.get_context_router())
    return router
