from sqlalchemy import select

from ..dependencies.session import ISession
from ..models.user_model import UserModel
from ..user_entity import UserEntity


class UserRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, user: UserEntity):
        instance = UserModel(**user.__dict__)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get(self, pk: int):
        stmt = select(UserModel).filter_by(id=pk)
        raw = await self.session.execute(stmt)
        return raw.scalar_one_or_none()

    async def get_list(self, limit: int):
        stmt = select(UserModel).limit(limit)
        raw = await self.session.execute(stmt)
        return raw.scalars()

