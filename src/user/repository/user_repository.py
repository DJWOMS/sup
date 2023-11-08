from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from ..schema.user_schema import CreateUser
from ..models.user_model import UserModel


class UserRepository:
    async def create(self, db_session: Session, data: CreateUser, password):
        instance = UserModel(**data.model_dump(), password=password)
        db_session.add(instance)
        await db_session.commit()
        await db_session.refresh(instance)
        return instance
