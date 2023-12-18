from src.mit.dependencies.repositories import IMitRepository
from src.mit.mit_dto import CreateUserMeet


class MitService:

    def __init__(self, repository: IMitRepository):
        self.repository = repository

    async def was_not_was(self, dto: CreateUserMeet):
        return await self.repository.was_not_was(dto)


