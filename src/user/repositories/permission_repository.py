from sqlalchemy import select, update, delete

from ..dependencies.session import ISession
from ..dtos.permission_dto import CreatePermissionDTO, UpdatePermissionDTO
from ..models.permission_model import PermissionModel


class PermissionRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, dto: CreatePermissionDTO):
        instance = PermissionModel(**dto.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get_list(self, limit: int):
        stmt = select(PermissionModel).limit(limit)
        raw = await self.session.execute(stmt)
        return raw.scalars()

    async def update(self, dto: UpdatePermissionDTO, pk: int):
        stmt = (
            update(PermissionModel)
            .values(**dto.model_dump())
            .filter_by(id=pk)
            .returning(PermissionModel)
        )
        raw = await self.session.execute(stmt)
        await self.session.commit()
        return raw.scalar_one()

    async def delete(self, pk: int) -> None:
        stmt = delete(PermissionModel).where(PermissionModel.id == pk)
        await self.session.execute(stmt)
        await self.session.commit()
