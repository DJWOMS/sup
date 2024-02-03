from src.app.dependencies.repositories import IRoleRepository
from src.domain.role.role_dto import CreateRoleDTO, UpdateRoleDTO


class RoleService:

    def __init__(self, repository: IRoleRepository):
        self.repository = repository

    async def create(self, dto: CreateRoleDTO):
        return await self.repository.create(dto)

    async def get_list(self, limit: int):
        return await self.repository.get_list(limit)

    async def get(self, pk: int):
        return await self.repository.get(pk)

    async def update(self, pk: int, dto: UpdateRoleDTO):
        return await self.repository.update(dto, pk)

    async def delete(self, pk: int):
        return await self.repository.delete(pk)
