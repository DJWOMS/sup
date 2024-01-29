from typing import Annotated
from fastapi import Depends

from ..infra.repositories.invitation_repository import InvitationRepository
from ..infra.repositories.email_repository import EmailRepository
from ..infra.repositories.login_repository import LoginRepository
from ..infra.repositories.meet_repository import MeetRepository
from ..infra.repositories.permission_repository import PermissionRepository
from ..infra.repositories.role_repository import RoleRepository
from ..infra.repositories.user_repository import UserRepository


IUserRepository = Annotated[UserRepository, Depends()]
IRoleRepository = Annotated[RoleRepository, Depends()]
IPermissionRepository = Annotated[PermissionRepository, Depends()]
IMeetRepository = Annotated[MeetRepository, Depends()]
ILoginRepository = Annotated[LoginRepository, Depends()]
IEmailRepository = Annotated[EmailRepository, Depends()]
IInvitationRepository = Annotated[InvitationRepository, Depends()]

