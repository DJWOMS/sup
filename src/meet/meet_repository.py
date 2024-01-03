from sqlalchemy import select, update, delete
from sqlalchemy.orm import selectinload, joinedload

from src.meet.meet_dto import CreateMeetDTO, MeetResponseDTO, UserMeetResponseDTO
from src.meet.meet_model import UserMeetModel, MeetModel
from src.user.dependencies.session import ISession
from src.user.models.user_model import UserModel


class MeetRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, dto: CreateMeetDTO):
        instance = MeetModel(**dto.model_dump(exclude={'users'}))
        _users = [UserMeetModel(**user.model_dump(), meet_id=instance.id) for user in dto.users]
        instance.users.append(*_users)
        self.session.add_all([instance, *_users])
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get(self, pk: int):
        stmt = select(MeetModel).filter_by(id=pk).options(
           selectinload(MeetModel.users).selectinload(UserMeetModel.user)
        )
        result = await self.session.execute(stmt)
        return self.to_dto(result.unique().scalar_one_or_none())

    def to_dto(self, instance: MeetModel):
        users = [
            UserMeetResponseDTO(
                id=user.user.id,
                name=user.user.name,
                name_telegram=user.user.name_telegram,
                nick_telegram=user.user.nick_telegram,
                color=user.color
            )
            for user in instance.users
        ]
        return MeetResponseDTO(
            id=instance.id,
            title=instance.title,
            date=instance.date,
            users=users
        )
