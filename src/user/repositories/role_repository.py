from sqlalchemy import select, delete, update

from src.user.dependencies.session import ISession
from src.user.dtos.role_dto import CreateRoleDTO, UpdateRoleDTO
from src.user.models.role_model import RoleModel


class RoleRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, dto: CreateRoleDTO):
        instance = RoleModel(**dto.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get_list(self, limit: int):
        stmt = select(RoleModel).limit(limit)
        raw = await self.session.execute(stmt)
        return raw.scalars()

    async def get(self, pk: int):
        stmt = select(RoleModel).filter_by(id=pk)
        raw = await self.session.execute(stmt)
        return raw.scalar_one_or_none()

    async def update(self, dto: UpdateRoleDTO, pk: int):
        stmt = update(RoleModel).values(**dto.model_dump()).filter_by(id=pk).returning(RoleModel)
        raw = await self.session.execute(stmt)
        await self.session.commit()
        return raw.scalar_one()

    async def delete(self, pk: int) -> None:
        stmt = delete(RoleModel).where(RoleModel.id == pk)
        await self.session.execute(stmt)
        await self.session.commit()
