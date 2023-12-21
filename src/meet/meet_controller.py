from fastapi import APIRouter

from src.meet.dependencies.services import IMeetService
from src.meet.meet_dto import CreateUserMeet, MeetBase

router = APIRouter(prefix="/meet", tags=["meet"])


@router.post("/user_meet", response_model=MeetBase)
async def user_meet(dto: CreateUserMeet, service: IMeetService):
    return await service.create(dto)
