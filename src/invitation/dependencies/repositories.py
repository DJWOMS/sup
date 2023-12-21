from typing import Annotated
from fastapi import Depends

from src.invitation.invitation_repository import InvitationRepository

IInvitationRepository = Annotated[InvitationRepository, Depends()]

