from typing import Annotated
from fastapi import Depends

from src.user.user_service import UserService


IUserService = Annotated[UserService, Depends()]
