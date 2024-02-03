from src.app.dependencies.repositories import IPermissionRepository
from src.domain.permission.permission_dto import (
    CreatePermissionDTO,
    UpdatePermissionDTO,
    GetPermissionListDTO
)


class PermissionService:

    def __init__(self, repository: IPermissionRepository):
        self.repository = repository

    async def create(self, dto: CreatePermissionDTO):
        return await self.repository.create(dto)

    async def get_list(self, limit: int) -> GetPermissionListDTO:
        return await self.repository.get_list(limit)

    async def update(self, pk: int, dto: UpdatePermissionDTO):
        return await self.repository.update(dto, pk)

    async def delete(self, pk: int):
        return await self.repository.delete(pk)
