from typing import Annotated
from fastapi import Depends

from src.role.role_repository import RoleRepository


IRoleRepository = Annotated[RoleRepository, Depends()]
