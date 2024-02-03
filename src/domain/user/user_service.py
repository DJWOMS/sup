from src.app.dependencies.repositories import IEmailRepository
from src.app.dependencies.repositories import IUserRepository
from src.domain.user.user_dto import CreateUserDTO, UpdateUserDTO, UpdatePasswordDTO
from src.domain.user.user_entity import UserEntity
from src.domain.email.email_dto import CreateEmailCodeDTO


class UserService:

    def __init__(self, repository: IUserRepository,
                 email_repository: IEmailRepository,
                 ):
        self.repository = repository
        self.email_repository = email_repository

    async def create(self, dto: CreateUserDTO):
        user = UserEntity(**dto.model_dump())
        user = user.get_new_hash_password()
        user_verify = user.create_verify_code()
        user = await self.repository.create(user)
        await self.email_repository.create(CreateEmailCodeDTO(user_id=user.id, code=user_verify))
        return user

    async def get_list(self, limit: int):
        return await self.repository.get_list(limit)

    async def get(self, pk: int):
        return await self.repository.get(pk)

    async def update(self, pk: int, dto: UpdateUserDTO):
        return await self.repository.update(dto, pk)

    async def delete(self, pk: int):
        return await self.repository.delete(pk)

    async def update_pass(self, pk: int, dto: UpdatePasswordDTO):
        new_password = UserEntity.set_password(dto.password)
        return await self.repository.update_pass(new_password, pk)
