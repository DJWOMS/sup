import logging

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI

from src.app.config.project_config import settings as main_settings
from src.app.config.swagger_config import settings as swagger_settings
from src.app.config.logging_config import settings as logger_settings, logger_config

from src.app.hooks import on_app_startup, on_app_shutdown

from src.app.middleware import init_middleware
from src.app.routers import init_routers


@asynccontextmanager
async def lifespan(application: FastAPI):
    # BEFORE_STARTUP
    if main_settings.hooks_enabled:
        await on_app_startup(application)
    else:
        pass
    yield
    # AFTER_STARTUP
    if main_settings.hooks_enabled:
        await on_app_shutdown(application)
    else:
        pass


def get_description(path: Path | str) -> str:

    return path.read_text("UTF-8") if isinstance(path, Path) else Path(path).read_text("UTF-8")


def get_application() -> FastAPI:
    # if logger_settings.logging_on:
    #     logging.config.dictConfig(logger_config)  # noqa
    application = FastAPI(
        title=swagger_settings.title,
        # description=get_description(swagger_settings.description),
        summary=swagger_settings.summary,
        version=main_settings.version,
        terms_of_service=swagger_settings.terms_of_service,
        contact=swagger_settings.contact,
        license_info=swagger_settings.license,
        lifespan=lifespan,
        root_path=main_settings.root_path,
        debug=main_settings.debug,
        docs_url=swagger_settings.docs_url if main_settings.debug else None,
        redoc_url=swagger_settings.redoc_url if main_settings.debug else None,
        openapi_url=f"{swagger_settings.docs_url}/openapi.json" if main_settings.debug else None,
    )
    # ---------------MIDDLEWARE---------------
    init_middleware(application)
    # ----------------ROUTERS---------------
    init_routers(application)
    # ----------------END---------------
    return application
