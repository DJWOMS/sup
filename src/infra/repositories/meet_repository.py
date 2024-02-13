from sqlalchemy import select, update, delete
from sqlalchemy.orm import selectinload, joinedload

from src.lib.exceptions import NotFoundError
from src.domain.meet.meet_dto import (
    CreateMeetDTO,
    UpdateMeetDTO,
    MeetResponseDTO,
    UserMeetResponseDTO
)

from ..database.session import ISession
from ..models.meet_model import MeetModel
from ..models.user_meet_model import UserMeetModel


class MeetRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, dto: CreateMeetDTO):
        meet = MeetModel(**dto.model_dump(exclude={"users"}))
        self.session.add(meet)
        await self.session.commit()
        await self.session.refresh(meet)
        return self.to_dto(meet)

    # TODO  Переписать метод update еще не дописано

    async def update(self, pk: int, dto: UpdateMeetDTO):
        stmt = update(MeetModel).filter_by(id=pk).values(**dto.model_dump(exclude={"users"}))
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
        stmt = delete(MeetModel).where(MeetModel.id == pk)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount

    async def get(self, pk: int):
        stmt = select(MeetModel).filter_by(id=pk).options(
            selectinload(MeetModel.users).selectinload(UserMeetModel.user)
        )
        result = await self.session.execute(stmt)
        instance = result.scalars().first()
        if instance:
            return instance
        else:
            raise NotFoundError("Meet не найден")

    def to_dto(self, instance: MeetModel):
        return MeetResponseDTO(id=instance.id, title=instance.title, date=instance.date)