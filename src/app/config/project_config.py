from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: str = Field(alias="APP_HOST")
    port: int = Field(alias="APP_PORT")
    debug: bool = Field(default=False, alias="APP_DEBUG")
    version: str = Field(alias="APP_VERSION")
    hooks_enabled: bool = Field(default=True, alias="APP_HOOKS_ENABLED")
    root_path: str = Field(default="", alias="APP_ROOT_PATH")
    timezone_shift: int = Field(default=3, alias="APP_TIMEZONE_SHIFT")


settings = Settings()
