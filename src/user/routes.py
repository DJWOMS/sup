from fastapi import APIRouter
from . import user_controller


def get_context_router():
    router = APIRouter()
    router.include_router(user_controller.router)
    return router
