from sqlalchemy.orm import Session

from ..dependencies.repositories import IRoleRepository

from src.user.repositories.role_repository import RoleRepository
from src.user.dtos.role_dto import CreateRole


class RoleService:

    def __init__(self, repository: IRoleRepository):
        self.repository = repository

    async def create(self, dto: CreateRole):
        return await self.repository.create(dto)
