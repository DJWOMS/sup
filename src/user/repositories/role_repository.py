from sqlalchemy import select

from src.user.dependencies.session import ISession
from src.user.dtos.role_dto import CreateRole
from src.user.models.role_model import RoleModel


class RoleRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, dto: CreateRole):
        instance = RoleModel(**dto.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get(self, pk: int):
        stmt = select(RoleModel).filter_by(id=pk)
        raw = await self.session.execute(stmt)
        return raw.scalar_one_or_none()

    async def get_list(self):
        stmt = select(RoleModel)
        raw = await self.session.execute(stmt)
        return raw.scalars()
