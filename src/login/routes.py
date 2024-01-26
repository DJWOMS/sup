from fastapi import APIRouter

from ..login import login_controller


def get_context_router():
    router = APIRouter()
    router.include_router(login_controller.router)
    return router
