from abc import ABC, abstractmethod
from typing import Type

from pydantic import BaseModel
from sqlalchemy import insert, select, update, delete, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.models.base_model import Base


class Repository(ABC):

    """ Абстрактный CRUD - репозиторий """

    @abstractmethod
    async def create(self):
        pass

    @abstractmethod
    async def get_list(self, limit: int, offset: int):
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

    """
    CRUD - репозиторий для SQLAlchemy
    При инициализации наследников определяется модель и стандартное dto ответа
    """

    model: Type[Base] = None
    response_dto: BaseModel = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, create_dto: BaseModel, response_dto: Base | None = None) -> BaseModel:
        async with self.session() as session:
            stmt = insert(self.model).values(**create_dto.model_dump()).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return self.to_dto(res.scalar_one(), response_dto)

    async def get_one(self, response_dto: Base | None = None, **filters) -> BaseModel:
        async with self.session() as session:
            stmt = select(self.model).filter_by(**filters)
            result = await session.execute(stmt)
            instance = result.scalar_one_or_none()
            return self.to_dto(instance, response_dto) if instance else instance

    async def get_list(
            self,
            response_dto: Base | None = None,
            limit: int = 100,
            offset: int = 0,
            order: str = "id"
                    ) -> list[BaseModel]:
        async with self.session() as session:
            stmt = select(self.model).order_by(order).limit(limit).offset(offset)
            res = await session.execute(stmt)
            return self.to_dto(res, response_dto)

    async def update(self, update_dto: BaseModel, response_dto: Base | None = None, **filters) -> BaseModel:
        async with self.session() as session:
            stmt = update(self.model).values(**update_dto).filter_by(**filters).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return self.to_dto(res.scalar_one(), response_dto)

    async def delete(self, **filters) -> None:
        async with self.session() as session:
            stmt = delete(self.model).filter_by(**filters)
            await session.execute(stmt)
            await session.commit()

    def to_dto(self, instance: Base | ScalarResult, dto: BaseModel = None) -> BaseModel | list[BaseModel]:
        """
        Метод, преобразующий модели SQLAlchemy к dto.
        """
        if not dto:
            dto = self.response_dto
        if not isinstance(instance, ScalarResult | list):
            return dto.model_validate(instance, from_attributes=True)
        return [dto.model_validate(row, from_attributes=True) for row in instance]
