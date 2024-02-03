from fastapi import APIRouter, HTTPException

from src.app.dependencies.services import IInvitationService
from src.lib.exceptions import InviteError
from src.domain.invitation.invitation_dto import (
    InvitationCreateDTO,
    GetInvitationListDTO,
    InvitationCheckCodeDTO
)


router = APIRouter(prefix="/invitation", tags=["invitation"])


@router.post("/", response_model=InvitationCreateDTO)
async def create_invitation(service: IInvitationService):
    return await service.create()


@router.get("/", response_model=list[GetInvitationListDTO])
async def get_list_invitation(service: IInvitationService):
    return await service.get_list()


@router.get("/", response_model=InvitationCheckCodeDTO)
async def check_code(code: str, service: IInvitationService):
    try:
        return await service.check(code)
    except InviteError as e:
        raise HTTPException(status_code=400, detail=str(e))
