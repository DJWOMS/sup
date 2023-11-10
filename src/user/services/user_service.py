from ..dependencies.repositories import IUserRepository
from src.user.dtos.user_dto import CreateUser, UpdateUser
from src.user.user_entity import UserEntity


class UserService:

    def __init__(self, repository: IUserRepository):
        self.repository = repository

    async def create(self, dto: CreateUser):
        user = UserEntity(**dto.model_dump()).get_new_hash_password()
        return await self.repository.create(user)

    async def update(self, pk: int, dto: UpdateUser):
        return await self.repository.update(dto, pk)

    async def delete(self, pk: int):
        return await self.repository.delete(pk)

    async def get(self, pk: int):
        return await self.repository.get(pk)

    async def get_list(self, limit: int):
        return await self.repository.get_list(limit)
