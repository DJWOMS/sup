from sqlalchemy import delete, select

from src.infra.models.user_meet_model import UserMeetModel
from src.domain.meet.meet_dto import UserMeetDTO


class UserMeetRepository:
    def __init__(self, session):
        self.session = session

    async def create(self, dto: list[UserMeetDTO], meet_id: int):
        _users = []
        for user in dto:
            _user = UserMeetModel(meet_id=meet_id, user_id=user.user_id, color=user.color)
            _users.append(_user)
        self.session.add_all([*_users])
        await self.session.commit()
        return self.to_dto(_users)

    async def get(self, meet_id: int):
        stmt = select(UserMeetModel).where(UserMeetModel.meet_id == meet_id)
        result = await self.session.execute(stmt)
        user_meets = result.scalars().all()
        return self.to_dto(user_meets)

    async def delete(self, meet_id: int):
        stmt = delete(UserMeetModel).where(UserMeetModel.meet_id == meet_id)
        await self.session.execute(stmt)
        await self.session.commit()

    def to_dto(self, users: list[UserMeetModel]) -> list[UserMeetDTO]:
        for user in users:
            yield UserMeetDTO(
                user_id=user.user_id,
                color=user.color
            )
