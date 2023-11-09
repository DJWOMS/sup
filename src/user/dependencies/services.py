from typing import Annotated
from fastapi import Depends
from ..services.user_servise import UserService


IUserService = Annotated[UserService, Depends()]
