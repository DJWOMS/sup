
from pydantic import (
    Field,
    EmailStr,
    AnyUrl,
)

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    title: str = Field(default="СУП", alias="APP_TITLE")
    description: str | None = Field(default=None, alias="APP_DESCRIPTION")
    summary: str | None = Field(None, alias="APP_SUMMARY")
    terms_of_service: str | None = Field(None, alias="APP_TERMS_OF_SERVICE")
    licence_name: str = Field("Apache 2.0", alias="APP_LICENSE_NAME")
    licence_identifier: str = Field("MIT", alias="APP_LICENSE_IDENTIFIER")
    licence_url: AnyUrl | None = Field("https://www.apache.org/licenses/LICENSE-2.0.html", alias="APP_LICENSE_URL")
    contact_name: str | None = Field("Michael Omelchenko", alias="APP_CONTACT_NAME")
    contact_url: AnyUrl | None = Field("https://t.me/DJWOMS", alias="APP_CONTACT_URL")
    contact_email: EmailStr | None = Field("socanime@gmail.com", alias="APP_CONTACT_EMAIL")
    docs_url: str | None = Field(None, alias="APP_DOCS_URL")
    redoc_url: str | None = Field(None, alias="APP_REDOC_URL") # noqa

    @property
    def contact(self) -> dict:
        return {
            "name": self.contact_name,
            "url": self.contact_url,
            "email": self.contact_email
        }

    @property
    def license(self) -> dict:
        return {
            "name": self.licence_name,
            "url": self.licence_url,
            "identifier": self.licence_identifier
        }


settings = Settings()
