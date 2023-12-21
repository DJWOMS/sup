from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool
    SECRET_KEY: str
    CORS_ALLOWED_ORIGINS: str


settings = Settings()
