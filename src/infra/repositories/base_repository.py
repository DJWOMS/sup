from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseModel
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.models.base_model import Base


class Repository(ABC):

    @abstractmethod
    async def create(self):
        pass

    @abstractmethod
    async def get_list(self, limit:int, offset:int):
        pass

    @abstractmethod
    async def get_one(self):
        pass

    @abstractmethod
    async def update(self):
        pass

    @abstractmethod
    async def delete(self):
        pass


class SQLAlchemyRepository(Repository):


    def __init__(self, session: AsyncSession, model: Type[Base], dto: BaseModel):
        self.session = session
        self.model = model
        self.response_dto = dto

    async def create(self, create_dto: BaseModel):
        async with self.session() as session:
            stmt = insert(self.model).values(**create_dto.model_dump()).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return self.to_dto(self.response_dto, res.scalar_one())

    async def get_one(self, **filters):
        async with self.session() as session:
            stmt = select(self.model).filter_by(**filters)
            result = await session.execute(stmt)
            instance = result.scalar_one_or_none()
            return self.to_dto(self.response_dto, instance) if instance else instance

    async def get_list(self, limit: int = 100, offset: int = 0, order: str = "id"):
        async with self.session() as session:
            stmt = select(self.model).order_by(order).limit(limit).offset(offset)
            res = await session.execute(stmt)
            return [self.to_dto(self.response_dto, instance) for instance in res.scalar_all()]

    async def update(self, update_dto: BaseModel, **filters):
        async with self.session() as session:
            stmt = update(self.model).values(**update_dto).filter_by(**filters).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return self.to_dto(self.response_dto, res.scalar_one())

    async def delete(self, **filters) -> None:
        async with self.session() as session:
            stmt = delete(self.model).filter_by(**filters)
            await session.execute(stmt)
            await session.commit()

    @staticmethod
    def to_dto(dto: BaseModel, instance: Base):
        return dto.model_validate(instance, from_attributes=True)


