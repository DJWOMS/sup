from typing import Annotated
from fastapi import Depends

from src.user.user_repository import UserRepository


IUserRepository = Annotated[UserRepository, Depends()]
