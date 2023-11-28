from fastapi import APIRouter, HTTPException

from src.exceptions import InviteError
from src.invitation.invitation_dto import InvitationCreate, ResponseInvitationList, InvitationCheckCode
from src.invitation.dependencies.services import IInvitationService


router = APIRouter(prefix="/invitation", tags=["invitation"])


@router.post("/", response_model=InvitationCreate)
async def create_invitation(service: IInvitationService):
    return await service.create()


@router.get("/get_list", response_model=list[ResponseInvitationList])
async def get_list_invitation(service: IInvitationService):
    return await service.get_list()


@router.get("/", response_model=InvitationCheckCode)
async def check_code(code: str, service: IInvitationService):
    try:
        return await service.check(code)
    except InviteError as e:
        raise HTTPException(status_code=400, detail=str(e))
