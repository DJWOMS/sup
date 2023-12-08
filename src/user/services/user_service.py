from ..dependencies.repositories import IUserRepository, IEmailRepository, INotificationRepository
from src.user.dtos.user_dto import CreateUser, UpdateUser, UpdatePassword
from src.user.user_entity import UserEntity
from ..dtos.email__dto import CreateVerify


class UserService:

    def __init__(self, repository: IUserRepository,
                 email_repository: IEmailRepository,
                 send_repository: INotificationRepository
                 ):
        self.repository = repository
        self.email_repository = email_repository
        self.send_repository = send_repository

    async def create(self, dto: CreateUser):
        user = UserEntity(**dto.model_dump())
        user = user.get_new_hash_password()
        print(user.password, "$"*90)
        user_verify = user.create_verify_code()
        user = await self.repository.create(user)
        await self.email_repository.create(CreateVerify(user_id=user.id, code=user_verify))
        await self.send_repository.send_mail(user_verify=user_verify)
        return user

    async def update(self, pk: int, dto: UpdateUser):
        return await self.repository.update(dto, pk)

    async def update_pass(self, pk: int, dto: UpdatePassword):
        new_password = UserEntity.set_password(dto.password)
        return await self.repository.update_pass(new_password, pk)

    async def delete(self, pk: int):
        return await self.repository.delete(pk)

    async def get(self, pk: int):
        return await self.repository.get(pk)

    async def get_list(self, limit: int):
        return await self.repository.get_list(limit)
