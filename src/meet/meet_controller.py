from fastapi import APIRouter

from src.meet.dependencies.services import IMeetService
from src.meet.meet_dto import CreateMeetDTO, MeetBaseDTO

router = APIRouter(prefix="/meet", tags=["meet"])


@router.post("/", response_model=MeetBaseDTO)
async def create_meet(dto: CreateMeetDTO, service: IMeetService):
    return await service.create(dto)
