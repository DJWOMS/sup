from typing import Annotated
from fastapi import Depends

from src.invitation.invitation_service import InvitationService

IInvitationService = Annotated[InvitationService, Depends()]
