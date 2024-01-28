from typing import Annotated
from fastapi import Depends

from ..invitation.invitation_repository import InvitationRepository

IInvitationRepository = Annotated[InvitationRepository, Depends()]

