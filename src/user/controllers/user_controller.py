from fastapi import APIRouter

from ..dependencies.services import IUserService
from src.user.dtos.user_dto import CreateUser, ResponseUser, ResponseUserList, UpdateUser, UpdatePassword

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", response_model=ResponseUser)
async def create_user(dto: CreateUser, service: IUserService):
    return await service.create(dto)


@router.put("/{pk}", response_model=ResponseUser)
async def update_user(pk: int, dto: UpdateUser, service: IUserService):
    return await service.update(pk, dto)


@router.put("/password/{pk}", response_model=UpdatePassword)
async def update_pass(pk: int, dto: UpdatePassword, service: IUserService):
    return await service.update_pass(pk, dto)


@router.delete("/del/{pk}")
async def delete_message(pk: int, service: IUserService):
    return await service.delete(pk)


@router.get("/user/{pk}", response_model=ResponseUser)
async def get_user(pk: int, service: IUserService):
    return await service.get(pk)


@router.get("/get_list", response_model=list[ResponseUserList])
async def get_list_users(service: IUserService, limit: int = 50):
    return await service.get_list(limit)

