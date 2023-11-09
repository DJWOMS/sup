from fastapi import APIRouter
from .controllers import user_controller
from .controllers import role_controller


def get_context_router():
    router = APIRouter()
    router.include_router(user_controller.router)
    router.include_router(role_controller.router)
    return router
