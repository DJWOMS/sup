from typing import Annotated
from fastapi import Depends

from ..repositories.role_repository import RoleRepository
from ..repositories.user_repository import UserRepository


IUserRepository = Annotated[UserRepository, Depends()]
IRoleRepository = Annotated[RoleRepository, Depends()]
