from typing import Annotated
from fastapi import Depends

from src.email.email_repository import EmailRepository


IEmailRepository = Annotated[EmailRepository, Depends()]


