from typing import Annotated
from fastapi import Depends

from ..repositories.rights_repository import RightRepository
from ..repositories.role_repository import RoleRepository
from ..repositories.user_repository import UserRepository
from ..repositories.email_repository import EmailRepository
from ..services.notification_service import NotificationService

IUserRepository = Annotated[UserRepository, Depends()]
IRoleRepository = Annotated[RoleRepository, Depends()]
IEmailRepository = Annotated[EmailRepository, Depends()]
INotificationRepository = Annotated[NotificationService, Depends()]
IRightRepository = Annotated[RightRepository, Depends()]
