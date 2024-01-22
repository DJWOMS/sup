from typing import Annotated
from fastapi import Depends

from src.role.role_service import RoleService


IRoleService = Annotated[RoleService, Depends()]
