from pydantic import BaseModel
from datetime import date


class InvitationBase(BaseModel):
    code: str
    at_valid: date
    status: str = 'active'


class InvitationCreate(InvitationBase):
    pass


class ResponseInvitationList(InvitationBase):
    pass


class InvitationCheckCode(InvitationBase):
    pass
