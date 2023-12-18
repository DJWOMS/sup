from fastapi import APIRouter

from src.mit import mit_controller


def get_context_router():
    router = APIRouter()
    router.include_router(mit_controller.router)
    return router
