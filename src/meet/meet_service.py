from src.meet.dependencies.repositories import IMeetRepository
from src.meet.meet_dto import CreateMeetDTO


class MeetService:

    def __init__(self, repository: IMeetRepository):
        self.repository = repository

    async def create(self, dto: CreateMeetDTO):
        return await self.repository.create(dto)

    async def get(self, pk: int):
        return await self.repository.get(pk)

