from fastapi import APIRouter

from src.auth.auth_service import CurrentUser
from ..dependencies.services import IUserService
from src.user.user_dto import CreateUserDTO, GetUserDTO, GetUserListDTO, UpdateUserDTO, UpdatePasswordDTO

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", response_model=GetUserDTO)
async def create_user(dto: CreateUserDTO, service: IUserService):
    return await service.create(dto)


@router.get("/", response_model=list[GetUserListDTO])
async def get_list_users(current_user: CurrentUser, service: IUserService, limit: int = 50):
    if current_user:
        return await service.get_list(limit)
    return []


@router.get("/{pk}", response_model=GetUserDTO)
async def get_user(pk: int, service: IUserService):
    return await service.get(pk)


@router.put("/{pk}", response_model=GetUserDTO)
async def update_user(pk: int, dto: UpdateUserDTO, service: IUserService):
    return await service.update(pk, dto)


@router.delete("/{pk}")
async def delete_message(pk: int, service: IUserService):
    return await service.delete(pk)


@router.put("/{pk}/change_password", response_model=UpdatePasswordDTO)
async def update_pass(pk: int, dto: UpdatePasswordDTO, service: IUserService):
    return await service.update_pass(pk, dto)
