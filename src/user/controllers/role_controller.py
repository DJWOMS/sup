from fastapi import APIRouter

from ..dependencies.services import IRoleService
from src.user.dtos.role_dto import CreateRole, ResponseRole, ResponseRoleList

router = APIRouter(prefix="/role", tags=["role"])


@router.post("/", response_model=CreateRole)
async def create_role(dto: CreateRole, service: IRoleService):
    return await service.create(dto)


@router.get("/user/{pk}", response_model=ResponseRole)
async def get_user(pk: int, service: IRoleService):
    return await service.get(pk)


@router.get("/", response_model=list[ResponseRoleList])
async def get_list_users(service: IRoleService, limit: int = 10):
    return await service.get_list(limit)
