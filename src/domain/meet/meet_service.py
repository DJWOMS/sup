from ..dependencies.repositories import IMeetRepository
from src.meet.meet_dto import CreateMeetDTO, UpdateMeetDTO, MeetResponseDTO, MeetDTO


class MeetService:

    def __init__(self, repository: IMeetRepository):
        self.repository = repository

    async def create(self, dto: CreateMeetDTO) -> MeetDTO:
        return await self.repository.create(dto)

    async def update(self, pk: int, dto: UpdateMeetDTO) -> MeetResponseDTO:
        return await self.repository.update(pk, dto)

    async def delete(self, pk: int) -> None:
        return await self.repository.delete(pk)

    async def get(self, pk: int) -> MeetResponseDTO:
        return await self.repository.get(pk)

