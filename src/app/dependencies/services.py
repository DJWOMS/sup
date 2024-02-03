from typing import Annotated
from fastapi import Depends

from src.domain.invitation.invitation_service import InvitationService
from src.domain.email.email_service import EmailService
from src.domain.login.login_service import LoginService
from src.domain.meet.meet_service import MeetService
from src.domain.permission.permission_service import PermissionService
from src.domain.role.role_service import RoleService
from src.domain.user.user_service import UserService


IUserService = Annotated[UserService, Depends()]
IRoleService = Annotated[RoleService, Depends()]
IPermissionService = Annotated[PermissionService, Depends()]
IMeetService = Annotated[MeetService, Depends()]
ILoginService = Annotated[LoginService, Depends()]
IEmailService = Annotated[EmailService, Depends()]
IInvitationService = Annotated[InvitationService, Depends()]
