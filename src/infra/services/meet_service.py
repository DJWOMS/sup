from src.domain.meet.meet_dto import CreateMeetDTO, MeetDTO, MeetResponseDTO, UpdateMeetDTO, UserMeetResponseDTO
from src.infra.models.meet_model import MeetModel
from src.infra.models.user_meet_model import UserMeetModel
from src.infra.repositories.meet_repository import MeetRepository
from src.lib.exceptions import NotFoundError


class MeetService:
    def __init__(self, meet_repository: MeetRepository):
        self.meet_repository = meet_repository

    async def create(self, dto: CreateMeetDTO) -> MeetDTO:
        instance = MeetModel(**dto.model_dump(exclude={"users"}))
        _users = []
        for user in dto.users:
            _user = UserMeetModel(meet_id=instance.id, user_id=user.user_id, color=user.color)
            _users.append(_user)
            instance.users.append(_user)
        return await self.meet_repository.create(dto)

    async def update(self, pk: int, dto: UpdateMeetDTO) -> MeetDTO:
        pass

    async def delete(self, pk: int) -> MeetResponseDTO:
        check_meet = await self.meet_repository.get(pk)
        if not check_meet:
            raise NotFoundError("Meet не найден")
        return await self.meet_repository.delete(pk)

    async def get(self, pk: int) -> MeetResponseDTO:
        meet_instance = await self.meet_repository.get(pk)
        return self.to_dto_with_users(meet_instance)

    def to_dto_with_users(self, instance: MeetModel) -> MeetResponseDTO:
        users = [
            UserMeetResponseDTO(
                id=user_meet.user.id,
                name=user_meet.user.name,
                name_telegram=user_meet.user.name_telegram,
                nick_telegram=user_meet.user.nick_telegram,
                color=user_meet.color
            ) for user_meet in instance.users
        ]
        return MeetResponseDTO(
            id=instance.id,
            title=instance.title,
            date=instance.date,
            users=users
        )
