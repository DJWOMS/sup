from datetime import date

from src.exceptions import InviteError
from src.invitation.invitation_dto import InvitationCreate
from src.invitation.invitation_entity import InvitationEntity
from src.invitation.dependencies.repositories import IInvitationRepository


class InvitationService:

    def __init__(self, repository: IInvitationRepository):
        self.repository = repository

    async def create(self):
        invite = InvitationEntity()
        code = invite.generate_code()
        date = invite.date_generation()
        dto = InvitationCreate(code=code, at_valid=date)
        return await self.repository.create(dto)

    async def check(self, code: str):
        invite = await self.repository.get(code)
        at_date = date.today()
        if invite is None:
            raise InviteError("Not found")
        elif at_date > invite.at_valid:
            await self.repository.update("expired", invite.id)
            raise InviteError("Invalid date")
        elif invite.status == "visited":
            raise InviteError("Invalid status")

        invite = await self.repository.update("visited", invite.id)
        return invite

    async def get_list(self):
        return await self.repository.get_list()


# {
#     name: "addsd",
#     date: 26-36-2035,
#     users: [
#         {
#             user_id: 1,
#             color: red
#         },
#         {
#             user_id: 2,
#             color: red
#         }
#     ]
# }
