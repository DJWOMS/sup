from ..dependencies.repositories import IRoleRepository

from src.user.dtos.role_dto import CreateRole, UpdateRole


class RoleService:

    def __init__(self, repository: IRoleRepository):
        self.repository = repository

    async def create(self, dto: CreateRole):
        return await self.repository.create(dto)

    async def update(self, pk: int, dto: UpdateRole):
        return await self.repository.update(dto, pk)

    async def delete(self, pk: int):
        return await self.repository.delete(pk)

    async def get(self, pk: int):
        return await self.repository.get(pk)

    async def get_list(self, limit: int):
        return await self.repository.get_list(limit)
