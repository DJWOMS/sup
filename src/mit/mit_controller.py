from fastapi import APIRouter

from src.mit.dependencies.services import IMitService
from src.mit.mit_dto import CreateUserMeet

router = APIRouter(prefix="/mit", tags=["mit"])


@router.post("/user_mit", response_model=CreateUserMeet)
async def user_meet(dto: CreateUserMeet, service: IMitService):
    return await service.was_not_was(dto)
