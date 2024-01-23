from fastapi import APIRouter

from ..role import role_controller


def get_context_router():
    router = APIRouter()
    router.include_router(role_controller.router)
    return router
