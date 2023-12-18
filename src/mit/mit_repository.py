from src.mit.mit_dto import CreateUserMeet
from src.mit.mit_model import UserMeetModel
from src.user.dependencies.session import ISession


class MitRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def was_not_was(self, dto: CreateUserMeet):
        instance = UserMeetModel(**dto.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance
