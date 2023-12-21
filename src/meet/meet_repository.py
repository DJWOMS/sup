from src.meet.meet_dto import CreateUserMeet
from src.meet.meet_model import UserMeetModel
from src.user.dependencies.session import ISession


class MeetRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, dto: CreateUserMeet):
        instance = UserMeetModel(**dto.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance
