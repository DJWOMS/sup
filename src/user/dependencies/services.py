from typing import Annotated
from fastapi import Depends

from ..services.role_service import RoleService
from ..services.user_service import UserService

IUserService = Annotated[UserService, Depends()]
IRoleService = Annotated[RoleService, Depends()]

