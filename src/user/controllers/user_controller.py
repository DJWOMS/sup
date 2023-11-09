from fastapi import APIRouter

from ..dependencies.services import IUserService
from src.user.dtos.user_dto import CreateUser, ResponseUser, ResponseUserList

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", response_model=CreateUser)
async def create_user(dto: CreateUser, service: IUserService) -> CreateUser:
    return await service.create(dto)


@router.get("/user/{pk}", response_model=ResponseUser)
async def get_user(pk: int, service: IUserService):
    return await service.get(pk)


@router.get("/", response_model=list[ResponseUserList])
async def get_list_users(service: IUserService):
    return await service.get_list()

