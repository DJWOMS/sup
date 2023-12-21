from ..dependencies.repositories import IPermissionRepository
from ..dtos.permission_dto import CreatePermissionDTO, UpdatePermissionDTO, ResponsePermissionListDTO


class PermissionService:

    def __init__(self, repository: IPermissionRepository):
        self.repository = repository

    async def create(self, dto: CreatePermissionDTO):
        return await self.repository.create(dto)

    async def update(self, pk: int, dto: UpdatePermissionDTO):
        return await self.repository.update(dto, pk)

    async def delete(self, pk: int):
        return await self.repository.delete(pk)

    async def get_list(self, limit: int) -> ResponsePermissionListDTO:
        return await self.repository.get_list(limit)
