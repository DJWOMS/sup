from fastapi import APIRouter

from ..permission import permission_controller


def get_context_router():
    router = APIRouter()
    router.include_router(permission_controller.router)
    return router
