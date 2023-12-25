from sqlalchemy import select, update, delete

from ..dependencies.session import ISession
from ..dtos.user_dto import UpdateUserDTO
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

    async def get_list(self, limit: int):
        stmt = select(UserModel).limit(limit)
        raw = await self.session.execute(stmt)
        return raw.scalars()

    async def get(self, pk: int):
        stmt = select(UserModel).filter_by(id=pk)
        raw = await self.session.execute(stmt)
        return raw.scalar_one_or_none()

    async def update(self, dto: UpdateUserDTO, pk: int):
        stmt = update(UserModel).values(**dto.model_dump()).filter_by(id=pk).returning(UserModel)
        raw = await self.session.execute(stmt)
        await self.session.commit()
        return raw.scalar_one()

    async def delete(self, pk: int) -> None:
        stmt = delete(UserModel).where(UserModel.id == pk)
        await self.session.execute(stmt)
        await self.session.commit()

    async def update_active(self, active: bool, pk: int):
        stmt = update(UserModel).values(active=active).filter_by(id=pk).returning(UserModel)
        raw = await self.session.execute(stmt)
        await self.session.commit()
        return raw.scalar_one()

    async def update_pass(self, new_password: str, pk: int):
        stmt = update(UserModel).values(password=new_password).filter_by(id=pk).returning(UserModel)
        raw = await self.session.execute(stmt)
        await self.session.commit()
        return raw.scalar_one()





