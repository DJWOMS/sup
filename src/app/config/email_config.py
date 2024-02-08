from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # credentials
    email_username: str = Field(..., alias="EMAIL_USERNAME")
    email_password: str = Field(..., alias="EMAIL_PASSWORD")

    # server config

    smtp_port: int = Field(465, alias="SMTP_PORT")
    smtp_host: str = Field("smtp.gmail.com", alias="SMTP_HOST")


settings = Settings()
