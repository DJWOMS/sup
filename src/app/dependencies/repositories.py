from typing import Annotated
from fastapi import Depends

from src.infra.repositories.invitation_repository import InvitationRepository
from src.infra.repositories.email_repository import EmailRepository
from src.infra.repositories.login_repository import LoginRepository
from src.infra.repositories.meet_repository import MeetRepository
from src.infra.repositories.permission_repository import PermissionRepository
from src.infra.repositories.role_repository import RoleRepository
from src.infra.repositories.user_repository import UserRepository
from src.infra.repositories.usermeet_repository import UserMeetRepository


IUserRepository = Annotated[UserRepository, Depends()]
IRoleRepository = Annotated[RoleRepository, Depends()]
IPermissionRepository = Annotated[PermissionRepository, Depends()]
IMeetRepository = Annotated[MeetRepository, Depends()]
ILoginRepository = Annotated[LoginRepository, Depends()]
IEmailRepository = Annotated[EmailRepository, Depends()]
IInvitationRepository = Annotated[InvitationRepository, Depends()]
IUserMeetRepository = Annotated[UserMeetRepository, Depends()]
