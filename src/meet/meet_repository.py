from src.meet.meet_dto import CreateUserMeet, MeetBase, UserMeet
from src.meet.meet_model import UserMeetModel, MeetModel
from src.user.dependencies.session import ISession


class MeetRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, dto: CreateUserMeet):
        # TODO сделать создание одним запросом
        meet_dto = MeetBase(**dto.model_dump(exclude={'users'}))
        print(meet_dto, "a"*100)
        instance = await self.create_meet(meet_dto)
        await self.session.commit()
        await self.session.refresh(instance)
        await self.add_users(dto.users, instance.id)
        return instance

    async def create_meet(self, dto: MeetBase):
        instance = MeetModel(**dto.model_dump())
        self.session.add(instance)
        return instance

    async def add_users(self, users: list[UserMeet], pk: int):
        _users = [UserMeetModel(**user.model_dump(), meet_id=pk) for user in users]
        self.session.add_all(_users)
        await self.session.commit()
