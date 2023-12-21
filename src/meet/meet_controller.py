from fastapi import APIRouter

from src.meet.dependencies.services import IMeetService
from src.meet.meet_dto import CreateUserMeet

router = APIRouter(prefix="/meet", tags=["meet"])


@router.post("/user_meet", response_model=CreateUserMeet)
async def user_meet(dto: CreateUserMeet, service: IMeetService):
    return await service.create(dto)
