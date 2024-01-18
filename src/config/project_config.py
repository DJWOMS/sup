from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool
    SECRET_KEY: str
    CORS_ALLOWED_ORIGINS: str
    SECRET_KEY: str = "HGDIYGS7gsguIGS*g&(SGcg&(*CGS*&C*SGC&*GCGCuo9shGpisudp9sU"
    API_V1_STR: str = "/api/v1"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8


settings = Settings()
