from fastapi import APIRouter

from src.app.dependencies.services import IPermissionService
from src.domain.permission.permission_dto import (
    CreatePermissionDTO,
    UpdatePermissionDTO,
    GetPermissionListDTO
)

router = APIRouter(prefix="/permissions", tags=["permissions"])


@router.post("/", response_model=CreatePermissionDTO)
async def create_permission(dto: CreatePermissionDTO, service: IPermissionService):
    return await service.create(dto)


@router.get("/", response_model=list[GetPermissionListDTO])
async def get_list_permission(service: IPermissionService, limit: int = 10):
    return await service.get_list(limit)


@router.put("/{pk}", response_model=UpdatePermissionDTO)
async def update_permission(pk: int, dto: UpdatePermissionDTO, service: IPermissionService):
    return await service.update(pk, dto)


@router.delete("/{pk}")
async def delete_permission(pk: int, service: IPermissionService):
    return await service.delete(pk)
