from sqlalchemy import select, update, delete
from sqlalchemy.orm import selectinload, joinedload

from src.exceptions import NotFoundError
from src.meet.meet_dto import UserMeetResponseDTO
from src.meet.meet_model import UserMeetModel, MeetModel
from src.user.dependencies.session import ISession
from src.user.models.user_model import UserModel


class UserMeetRepository(Repo):

    def __init__(self, session: ISession):
        self.session = session

    # async def create(self, dto: CreateMeetDTO):
    #     instance = MeetModel(**dto.model_dump(exclude={'users'}))
    #     _users = []
    #     for user in dto.users:
    #         _user = UserMeetModel(meet_id=instance.id, user_id=user.user_id, color=user.color)
    #         _users.append(_user)
    #         instance.users.append(_user)
    #     self.session.add_all([instance, *_users])
    #     await self.session.commit()
    #     await self.session.refresh(instance)
    #     return self.to_dto(instance)

    async def update(self, pk: int, dto: list[UserMeetResponseDTO]):
        stmt = update(MeetModel).filter_by(id=pk).values(**dto.model_dump(exclude={'users'}))
        result = await self.session.execute(stmt)
        if result.rowcount == 0:
            raise NotFoundError("Meet не найден")

        stmt = select(MeetModel).filter_by(id=pk).options(
            selectinload(MeetModel.users).selectinload(UserMeetModel.user)
        )
        result = await self.session.execute(stmt)
        updated_meet = result.scalar_one()

        for user in updated_meet.users:
            if not any(u.user_id == user.user_id for u in dto.users):
                updated_meet.users.remove(user)

        for user_data in dto.users:
            user = next((u for u in updated_meet.users if u.user_id == user_data.user_id), None)
            if user:
                user.color = user_data.color
            else:
                new_user = UserMeetModel(
                    meet_id=pk,
                    user_id=user_data.user_id,
                    color=user_data.color
                )
                result.users.append(new_user)
                self.session.add(new_user)

        await self.session.commit()
        await self.session.refresh(updated_meet)
        return self.to_dto(updated_meet)

    async def delete(self, pk: int):
        stmt = delete(MeetModel).filter_by(id=pk)
        result = await self.session.execute(stmt)
        if result.rowcount == 0:
            raise NotFoundError("Meet не найден")
        await self.session.commit()

    async def get(self, pk: int):
        stmt = select(MeetModel).filter_by(id=pk).options(
           joinedload(MeetModel.users).joinedload(UserMeetModel.user)
        )
        result = await self.session.execute(stmt)
        if instance := result.unique().scalar_one_or_none():
            return self.to_dto_with_users(instance)
        raise NotFoundError("Meet не найден")

    def to_dto(self, instance: MeetModel):
        return MeetResponseDTO(id=instance.id, title=instance.title, date=instance.date)

    # def to_dto_with_users(self, instance: MeetModel):
    #     users = [
    #         UserMeetResponseDTO(
    #             id=user_meet.user.id,
    #             name=user_meet.user.name,
    #             name_telegram=user_meet.user.name_telegram,
    #             nick_telegram=user_meet.user.nick_telegram,
    #             color=user_meet.color
    #         )
    #         for user_meet in instance.users
    #     ]
    #     return MeetResponseDTO(
    #         id=instance.id,
    #         title=instance.title,
    #         date=instance.date,
    #         users=users
    #     )
