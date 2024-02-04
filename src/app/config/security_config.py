from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str
    access_token_expire_minutes: int


settings = Settings()
