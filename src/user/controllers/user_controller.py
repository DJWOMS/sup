from fastapi import APIRouter

from ..dependencies.services import IUserService
from src.user.dtos.user_dto import CreateUser, UserResponse, UserList

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/")
async def create_user(dto: CreateUser, service: IUserService):
    return await service.create(dto)


@router.get("/user/{pk}", response_model=UserResponse)
async def get_user(pk: int, service: IUserService):
    return await service.get(pk)


@router.get("/", response_model=list[UserList])
async def get_list_users(service: IUserService):
    return await service.get_list()

