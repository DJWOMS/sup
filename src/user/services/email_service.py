from src.user.dependencies.repositories import IEmailRepository, IUserRepository


class EmailService:

    def __init__(self, repository: IEmailRepository, user_repository: IUserRepository):
        self.repository = repository
        self.user_repository = user_repository

    async def check(self, code: str):
        invite = await self.repository.get(code)
        await self.user_repository.update_active(active=True, pk=invite.user_id)
        return invite
