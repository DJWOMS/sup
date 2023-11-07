from sqlalchemy.orm import Session

from src.user.repository.user_repository import UserRepository
from src.user.schema.user_schema import CreateUser


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    async def create(self, data: CreateUser, db_session: Session):
        return await self.repository.create(db_session, data)
