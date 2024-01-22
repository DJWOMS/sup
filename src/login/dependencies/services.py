from typing import Annotated
from fastapi import Depends

from src.login.login_service import LoginService


ILoginService = Annotated[LoginService, Depends()]
