from fastapi import APIRouter

from src.dependencies.services import IRoleService
from src.role.role_dto import CreateRoleDTO, GetRoleDTO, GetRoleListDTO, UpdateRoleDTO

router = APIRouter(prefix="/role")


@router.post("/", response_model=GetRoleDTO)
async def create_role(dto: CreateRoleDTO, service: IRoleService):
    return await service.create(dto)


@router.get("/", response_model=list[GetRoleListDTO])
async def get_list_role(service: IRoleService, limit: int = 10):
    return await service.get_list(limit)


@router.get("/{pk}", response_model=GetRoleDTO)
async def get_role(pk: int, service: IRoleService):
    return await service.get(pk)


@router.put("/{pk}", response_model=GetRoleDTO)
async def update_role(pk: int, dto: UpdateRoleDTO, service: IRoleService):
    return await service.update(pk, dto)


@router.delete("/{pk}")
async def delete_role(pk: int, service: IRoleService):
    return await service.delete(pk)
