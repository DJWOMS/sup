from src.meet.meet_dto import CreateMeetDTO, MeetBaseDTO, UserDTO
from src.meet.meet_model import UserMeetModel, MeetModel
from src.user.dependencies.session import ISession


class MeetRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, dto: CreateMeetDTO):
        # TODO сделать создание одним запросом
        meet_dto = MeetBaseDTO(**dto.model_dump(exclude={'users'}))
        instance = await self.create_meet(meet_dto)
        await self.session.commit()
        await self.session.refresh(instance)
        await self.add_users(dto.users, instance.id)
        return instance

    async def create_meet(self, dto: MeetBaseDTO):
        instance = MeetModel(**dto.model_dump())
        self.session.add(instance)
        return instance

    async def add_users(self, users: list[UserDTO], pk: int):
        _users = [UserMeetModel(**user.model_dump(), meet_id=pk) for user in users]
        self.session.add_all(_users)
        await self.session.commit()
