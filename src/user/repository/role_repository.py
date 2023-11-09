from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession


from src.user.schema.role_schema import CreateRole
from src.user.models.role_model import RoleModel


class RoleRepository:
    async def create(self, db_session: AsyncSession, data: CreateRole):
        instance = RoleModel(**data.model_dump())
        db_session.add(instance)
        await db_session.commit()
        await db_session.refresh(instance)
        return instance

