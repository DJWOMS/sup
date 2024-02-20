from abc import ABC, abstractmethod

from typing import Type

from sqlalchemy import select, update, delete

from src.infra.database.session import ISession
from src.infra.models.base_model import Base

from pydantic import BaseModel


class BaseRepository(ABC):
    def __init__(self, session: ISession, model: Type[Base]):
        self.session = session
        self.model = model

    @abstractmethod
    async def create(self, dto: BaseModel):
        instance = self.model(**dto.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    @abstractmethod
    async def get_list(self, limit: int):
        stmt = select(self.model).limit(limit)
        raw = await self.session.execute(stmt)
        return raw.scalars()

    @abstractmethod
    async def get(self, pk: int):
        stmt = select(self.model).filter_by(id=pk)
        raw = await self.session.execute(stmt)
        return raw.scalar_one_or_none()

    @abstractmethod
    async def update(self, dto: BaseModel, pk: int):
        stmt = (
            update(self.model)
            .values(**dto.model_dump())
            .filter_by(id=pk)
            .returning(self.model)
        )
        raw = await self.session.execute(stmt)
        await self.session.commit()
        return raw.scalar_one()

    @abstractmethod
    async def delete(self, pk: int) -> None:
        stmt = delete(self.model).where(self.model.id == pk)
        await self.session.execute(stmt)
        await self.session.commit()






