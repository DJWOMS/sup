import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.project_config import settings
from src.api import (
    system_routes,
    v1_router,
)


def get_application() -> FastAPI:
    application = FastAPI(
        title="СУП",
        debug=settings.DEBUG,
        version="0.2.0"
    )
    application.include_router(system_routes, prefix="/system", tags=['system'])
    application.include_router(v1_router, prefix="/api/v1")

    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return application


app = get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
