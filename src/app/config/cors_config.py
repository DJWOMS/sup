from typing import List

from pydantic import Field

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    allow_origins: List[str] = Field(default=["*"], alias="CORS_ALLOW_ORIGINS")
    allow_methods: List[str] = Field(default=["GET"], alias="CORS_ALLOW_METHODS")
    allow_headers: List[str] = Field(default=[], alias="CORS_ALLOW_HEADERS")
    allow_credentials: bool = Field(default=False, alias="CORS_ALLOW_CREDENTIALS")
    allow_origin_regex: str | None = Field(None, alias="CORS_ALLOW_ORIGIN_REGEX")
    expose_headers: List[str] = Field(default=[], alias="CORS_EXPOSE_HEADERS")
    max_age: int = Field(default=600, alias="CORS_MAX_AGE")


settings = Settings()
