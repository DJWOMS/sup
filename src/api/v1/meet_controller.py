from typing import Annotated

from fastapi import APIRouter, Depends
from src.app.exception_handler import error_handler
from src.app.dependencies.services import IMeetService
from src.domain.meet.meet_dto import (
    CreateMeetDTO,
    UpdateMeetDTO,
    MeetDTO,
    MeetResponseDTO,
)
from src.domain.meet.meet_service import MeetService
from src.infra.database.session import ISession
from src.infra.repositories.meet_repository import MeetRepository
from src.infra.repositories.usermeet_repository import UserMeetRepository

router = APIRouter(prefix="/meet", tags=["meet"])

def provide_service(session: ISession):
    return MeetService(MeetRepository(session), UserMeetRepository(session))


@router.post("/", response_model=MeetDTO)
@error_handler
async def create_meet(dto: CreateMeetDTO, service: Annotated[MeetService, Depends(provide_service)]):
    return await service.create(dto)


@router.get("/{pk}", response_model=MeetResponseDTO)
@error_handler
async def get_meet(pk: int, service: IMeetService):
    return await service.get(pk)


@router.put("/{pk}", response_model=MeetResponseDTO)
@error_handler
async def update_meet(pk: int, dto: UpdateMeetDTO, service: IMeetService):
    return await service.update(pk, dto)


@router.delete("/{pk}", status_code=204)
@error_handler
async def delete_meet(pk: int, service: IMeetService):
    return await service.delete(pk)
