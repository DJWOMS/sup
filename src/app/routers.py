from fastapi import FastAPI
from src.api import (
    system_routes,
    v1_router,
)


def init_routers(app: FastAPI):
    app.include_router(system_routes, prefix="/system", tags=["system"])
    app.include_router(v1_router, prefix="/v1")
