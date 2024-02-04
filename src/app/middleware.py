from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.config.cors_config import settings as cors_settings


def init_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_settings.allow_origins,
        allow_credentials=cors_settings.allow_credentials,
        allow_methods=cors_settings.allow_methods,
        allow_headers=cors_settings.allow_headers,
        allow_origin_regex=cors_settings.allow_origin_regex,
        max_age=cors_settings.max_age,
    )
