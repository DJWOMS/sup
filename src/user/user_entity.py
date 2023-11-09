import secrets
import string
from dataclasses import dataclass

import argon2
from pydantic import EmailStr


@dataclass
class UserEntity:

    name: str
    surname: str
    email: EmailStr
    name_telegram: str
    nick_telegram: str
    nick_meet: str
    nick_gitlab: str
    nick_github: str
    role_id: int
    password: str | None = None

    def generate_password(self, length=20):
        character_sheet = string.ascii_letters + string.digits + '!@#$%^&*()_+=-'
        rand_pass = ''.join(secrets.choice(character_sheet)
                            for i in range(length))
        return rand_pass

    def hash_password(self, password: str) -> str:
        hashed = argon2.hash_password(password.encode('utf-8'))
        return hashed.decode('utf-8')

    def get_new_hash_password(self):
        password = self.generate_password()
        self.password = self.hash_password(password)
        return self

