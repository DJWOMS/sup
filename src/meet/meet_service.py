from src.meet.dependencies.repositories import IMeetRepository
from src.meet.meet_dto import CreateUserMeet


class MeetService:

    def __init__(self, repository: IMeetRepository):
        self.repository = repository

    async def create(self, dto: CreateUserMeet):
        return await self.repository.create(dto)



