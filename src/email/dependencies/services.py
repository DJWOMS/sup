from typing import Annotated
from fastapi import Depends

from src.email.email_service import EmailService


IEmailService = Annotated[EmailService, Depends()]
