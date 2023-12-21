from fastapi import APIRouter

from src.meet import meet_controller


def get_context_router():
    router = APIRouter()
    router.include_router(meet_controller.router)
    return router
