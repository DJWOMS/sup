from fastapi import APIRouter
from src.exception_handler import error_handler
from ..dependencies.services import IMeetService
from src.meet.meet_dto import CreateMeetDTO, UpdateMeetDTO, MeetDTO, MeetResponseDTO

router = APIRouter(prefix="/meet", tags=["meet"])


@router.post("/", response_model=MeetDTO)
@error_handler
async def create_meet(dto: CreateMeetDTO, service: IMeetService):
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
