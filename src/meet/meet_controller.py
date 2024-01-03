from fastapi import APIRouter

from src.meet.dependencies.services import IMeetService
from src.meet.meet_dto import CreateMeetDTO, MeetDTO, MeetResponseDTO

router = APIRouter(prefix="/meet", tags=["meet"])


@router.post("/", response_model=MeetDTO)
async def create_meet(dto: CreateMeetDTO, service: IMeetService):
    return await service.create(dto)


@router.get("/{pk}", response_model=MeetResponseDTO)
async def get_meet(pk: int, service: IMeetService):
    return await service.get(pk)
