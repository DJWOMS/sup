from ..dependencies.repositories import IRightRepository
from ..dtos.right_dto import CreateRight, UpdateRight


class RightsService:

    def __init__(self, repository: IRightRepository):
        self.repository = repository

    async def create(self, dto: CreateRight):
        return await self.repository.create(dto)

    async def update(self, pk: int, dto: UpdateRight):
        return await self.repository.update(dto, pk)

    async def delete(self, pk: int):
        return await self.repository.delete(pk)

    async def get_list(self, limit: int):
        return await self.repository.get_list(limit)
