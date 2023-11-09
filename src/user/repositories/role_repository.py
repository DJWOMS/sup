from src.user.dependencies.session import ISession
from src.user.dtos.role_dto import CreateRole
from src.user.models.role_model import RoleModel


class RoleRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, dto: CreateRole):
        instance = RoleModel(**dto.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

