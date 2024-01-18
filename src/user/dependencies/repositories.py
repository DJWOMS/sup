from typing import Annotated
from fastapi import Depends

from ..repositories.login_repository import LoginRepository
from ..repositories.permission_repository import PermissionRepository
from ..repositories.role_repository import RoleRepository
from ..repositories.user_repository import UserRepository
from ..repositories.email_repository import EmailRepository


IUserRepository = Annotated[UserRepository, Depends()]
IRoleRepository = Annotated[RoleRepository, Depends()]
IEmailRepository = Annotated[EmailRepository, Depends()]
IPermissionRepository = Annotated[PermissionRepository, Depends()]
ILoginRepository = Annotated[LoginRepository, Depends()]

