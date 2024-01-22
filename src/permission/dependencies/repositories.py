from typing import Annotated
from fastapi import Depends

from src.permission.permission_repository import PermissionRepository


IPermissionRepository = Annotated[PermissionRepository, Depends()]
