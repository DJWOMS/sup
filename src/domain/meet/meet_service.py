from src.app.dependencies.repositories import IMeetRepository, IUserMeetRepository
from src.domain.meet.meet_dto import CreateMeetDTO, MeetBaseDTO, UpdateMeetDTO, MeetResponseDTO, MeetDTO


class MeetService:

    def __init__(self, repository: IMeetRepository, usermeet_repository: IUserMeetRepository):
        self.repository = repository
        self.usermeet_repository = usermeet_repository

    async def create(self, dto: CreateMeetDTO) -> MeetDTO:
        meet = await self.repository.create(MeetBaseDTO(**dto.model_dump(exclude={"users"})))
        user_meet = await self.usermeet_repository.create(dto.users, meet.id)
        meet.users = user_meet
        return meet

    async def update(self, pk: int, dto: UpdateMeetDTO) -> MeetResponseDTO:
        return await self.repository.update(pk, dto)

    async def delete(self, pk: int) -> None:
        return await self.repository.delete(pk)

    async def get(self, pk: int) -> MeetResponseDTO:
        meet = await self.repository.get(pk)
        user_meet = await self.usermeet_repository.get(pk)
        get_meet = MeetResponseDTO(**meet.model_dump())
        get_meet.users = user_meet
        return get_meet

