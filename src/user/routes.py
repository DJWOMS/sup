from fastapi import APIRouter
from .controllers import user_controller
from .controllers import role_controller
from .controllers import permission_controller
from .controllers import login_controller
from .controllers import email_controller


def get_context_router():
    router = APIRouter()
    router.include_router(user_controller.router)
    router.include_router(role_controller.router)
    router.include_router(permission_controller.router)
    router.include_router(login_controller.router)
    router.include_router(email_controller.router)
    return router
