from fastapi import APIRouter

from .api import (
    email_controller,
    invitation_controller,
    login_controller,
    meet_controller,
    permission_controller,
    role_controller,
    user_controller,
)


def get_apps_router():
    router = APIRouter()
    router.include_router(permission_controller.router)
    router.include_router(role_controller.router)
    router.include_router(user_controller.router)
    router.include_router(email_controller.router)
    router.include_router(invitation_controller.router)
    router.include_router(login_controller.router)
    router.include_router(meet_controller.router)
    return router
