import secrets
import string

import argon2

from sqlalchemy.orm import Session

from src.user.repository.user_repository import UserRepository
from src.user.schema.user_schema import CreateUser


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    async def create(self, data: CreateUser, db_session: Session):
        password = self.hash_password()
        return await self.repository.create(db_session, data, password)

    def generate_password(self, length=20):
        character_sheet = string.ascii_letters + string.digits + '!@#$%^&*()_+=-'
        rand_pass = ''.join(secrets.choice(character_sheet)
                            for i in range(length))
        return rand_pass

    def hash_password(self) -> str:
        password = self.generate_password().encode('utf-8')
        hashed = argon2.hash_password(password)
        return hashed.decode('utf-8')




