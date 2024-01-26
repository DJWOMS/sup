from fastapi import APIRouter

from ..email import email_controller


def get_context_router():
    router = APIRouter()
    router.include_router(email_controller.router)
    return router
