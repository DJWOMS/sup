from typing import Annotated
from fastapi import Depends

from src.permission.permission_service import PermissionService


IPermissionService = Annotated[PermissionService, Depends()]
