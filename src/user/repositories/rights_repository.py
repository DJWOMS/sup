from sqlalchemy import select, update, delete

from ..dependencies.session import ISession
from ..dtos.right_dto import CreateRight, UpdateRight
from ..models.right_model import RightModel


class RightRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, dto: CreateRight):
        instance = RightModel(**dto.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def update(self, dto: UpdateRight, pk: int):
        stmt = update(RightModel).values(**dto.model_dump()).filter_by(id=pk).returning(RightModel)
        raw = await self.session.execute(stmt)
        await self.session.commit()
        return raw.scalar_one()

    async def delete(self, pk: int) -> None:
        stmt = delete(RightModel).where(RightModel.id == pk)
        await self.session.execute(stmt)
        await self.session.commit()

    async def get_list(self, limit: int):
        stmt = select(RightModel).limit(limit)
        raw = await self.session.execute(stmt)
        return raw.scalars()
