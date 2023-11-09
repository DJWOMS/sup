from sqlalchemy.orm import Session

from src.user.repository.role_repository import RoleRepository
from src.user.schema.role_schema import CreateRole


class RoleService:

    def __init__(self):
        self.repository = RoleRepository()

    async def create(self, data: CreateRole, db_session: Session):
        return await self.repository.create(db_session, data)
