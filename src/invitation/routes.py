from fastapi import APIRouter

from src.invitation import invitation_controller


def get_context_router():
    router = APIRouter()
    router.include_router(invitation_controller.router)
    return router
