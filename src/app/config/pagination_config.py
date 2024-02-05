from pydantic import Field

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    max_limit: int = Field(default=10000, alias="PAGINATION_MAX_LIMIT")


settings = Settings()
