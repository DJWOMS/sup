from typing import Annotated
from fastapi import Depends

from src.invitation.invitation_service import InvitationService
from src.email.email_service import EmailService
from src.login.login_service import LoginService
from src.meet.meet_service import MeetService
from src.permission.permission_service import PermissionService
from src.role.role_service import RoleService
from src.user.user_service import UserService


IUserService = Annotated[UserService, Depends()]
IRoleService = Annotated[RoleService, Depends()]
IPermissionService = Annotated[PermissionService, Depends()]
IMeetService = Annotated[MeetService, Depends()]
ILoginService = Annotated[LoginService, Depends()]
IEmailService = Annotated[EmailService, Depends()]
IInvitationService = Annotated[InvitationService, Depends()]
