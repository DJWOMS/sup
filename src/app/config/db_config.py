from pydantic import PostgresDsn, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url_scheme: str = Field("postgresql+asyncpg", alias="DB_URL_SCHEME")
    # host
    db_host: str = Field(..., alias="DB_HOST")
    db_port: str = Field(..., alias="DB_PORT")
    db_name: str = Field(..., alias="DB_NAME")
    # credentials
    db_user: str = Field(..., alias="DB_USER")
    db_password: str = Field(..., alias="DB_PASSWORD")
    # logging
    db_echo_log: bool = Field(False, alias="DB_ECHO_LOG")
    # run auto-migrate
    db_run_auto_migrate: bool = Field(False, alias="DB_RUN_AUTO_MIGRATE")

    @property
    def database_url(self) -> PostgresDsn:
        """ URL для подключения (DSN)"""
        return (
            f"{self.db_url_scheme}://{self.db_user}:{self.db_password}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}?async_fallback=True"
        )


settings = Settings()
