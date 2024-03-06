from abc import ABC, abstractmethod
from typing import Type, Any, Iterable

from pydantic import BaseModel
from sqlalchemy import (
    insert,
    select,
    update,
    delete,
    ScalarResult,
    Select,
    StatementLambdaElement,
    Result,
    Insert,
    ValuesBase,
    Delete,
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.models.base_model import Base
from src.lib.exceptions import NotFoundError


class Repository(ABC):
    """Абстрактный CRUD - репозиторий"""

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

    def __init__(
        self, session: AsyncSession, auto_commit: bool = None, auto_refresh: bool = None
    ):
        self.session = session
        self.auto_commit = auto_commit
        self.auto_refresh = auto_refresh

    async def create(
        self,
        create_dto: BaseModel,
        response_dto: Base | None = None,
        auto_commit: bool = True,
    ) -> BaseModel:
        stmt = (
            insert(self.model).values(**create_dto.model_dump()).returning(self.model)
        )
        res = await self._execute(stmt)
        await self._flush_or_commit(auto_commit)
        return self.to_dto(res.scalar_one(), response_dto)

    async def get_one(self, response_dto: Base | None = None, **filters) -> BaseModel:
        stmt = select(self.model).filter_by(**filters)
        result = await self._execute(stmt)
        instance = result.scalar_one_or_none()
        self.check_not_found(instance)
        return self.to_dto(instance, response_dto)

    async def get_list(
        self,
        response_dto: Base | None = None,
        limit: int = 100,
        offset: int = 0,
        order: str = "id",
    ) -> list[BaseModel]:
        stmt = select(self.model).order_by(order).limit(limit).offset(offset)
        res = await self._execute(stmt)
        return self.to_dto(res.scalars(), response_dto)

    async def update(
        self,
        update_dto: BaseModel,
        response_dto: Base | None = None,
        auto_commit: bool = True,
        **filters,
    ) -> BaseModel:
        stmt = (
            update(self.model)
            .values(**update_dto.model_dump())
            .filter_by(**filters)
            .returning(self.model)
        )
        res = (await self._execute(stmt)).scalar_one_or_none()
        self.check_not_found(res)
        await self._flush_or_commit(auto_commit)
        return self.to_dto(res, response_dto)

    async def delete(self, auto_commit: bool = True, **filters) -> None:
        stmt = delete(self.model).filter_by(**filters)
        result = await self._execute(stmt)
        if result.rowcount == 0:
            raise NotFoundError(
                f"По данным запроса в таблице {self.model.__tablename__} записей не найдено"
            )
        await self._flush_or_commit(auto_commit)

    def to_dto(
        self, instance: Base | ScalarResult, dto: BaseModel = None
    ) -> BaseModel | list[BaseModel]:
        """
        Метод, преобразующий модели SQLAlchemy к dto.
        """
        if dto is None:
            dto = self.response_dto
        if not isinstance(instance, ScalarResult | list):
            return dto.model_validate(instance, from_attributes=True)
        return [dto.model_validate(row, from_attributes=True) for row in instance]

    async def _flush_or_commit(self, auto_commit: bool | None) -> None:
        if auto_commit is None:
            auto_commit = self.auto_commit
        return (
            await self.session.commit() if auto_commit else await self.session.flush()
        )

    async def _refresh(
        self,
        instance: Base,
        auto_refresh: bool | None,
        attribute_names: Iterable[str] | None = None,
        with_for_update: bool | None = None,
    ) -> None:
        if auto_refresh is None:
            auto_refresh = self.auto_refresh

        return (
            await self.session.refresh(
                instance,
                attribute_names=attribute_names,
                with_for_update=with_for_update,
            )
            if auto_refresh
            else None
        )

    @staticmethod
    def check_not_found(item_or_none: Base | None) -> Base:
        if item_or_none is None:
            msg = "No item found when one was expected"
            raise NotFoundError(msg)
        return item_or_none

    async def _execute(
        self, statement: ValuesBase | Select[Any] | Delete
    ) -> Result[Any]:
        return await self.session.execute(statement)
