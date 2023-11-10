from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from ..dependencies.services import IUserService
from src.user.dtos.user_dto import CreateUser, ResponseUser, ResponseUserList, UpdateUser

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", response_model=CreateUser)
async def create_user(dto: CreateUser, service: IUserService):
    return await service.create(dto)


@router.put("/{pk}", response_model=UpdateUser)
async def update_user(pk: int, dto: UpdateUser, service: IUserService):
    return await service.update(pk, dto)


@router.delete("/{pk}")
async def delete_message(pk: int, service: IUserService):
    try:
        return await service.delete(pk)
    except ValueError as e:
        return HTTPException(status_code=HTTP_400_BAD_REQUEST)


@router.get("/user/{pk}", response_model=ResponseUser)
async def get_user(pk: int, service: IUserService):
    return await service.get(pk)


@router.get("/", response_model=list[ResponseUserList])
async def get_list_users(service: IUserService, limit: int = 50):
    return await service.get_list(limit)

