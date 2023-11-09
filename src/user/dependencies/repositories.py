from typing import Annotated
from fastapi import Depends
from ..repositories.user_repository import UserRepository


IUserRepository = Annotated[UserRepository, Depends()]
