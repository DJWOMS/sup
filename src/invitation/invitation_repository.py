from sqlalchemy import select, update

from src.invitation.invitation_dto import InvitationCreateDTO
from src.invitation.invitation_model import InvitationModel
from src.user.dependencies.session import ISession


class InvitationRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, dto: InvitationCreateDTO):
        instance = InvitationModel(**dto.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get_list(self):
        stmt = select(InvitationModel)
        raw = await self.session.execute(stmt)
        return raw.scalars()

    async def update(self, status: str, pk: int):
        stmt = update(InvitationModel).values(status=status).filter_by(id=pk).returning(InvitationModel)
        raw = await self.session.execute(stmt)
        await self.session.commit()
        return raw.scalar_one()
