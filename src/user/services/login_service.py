from ..dependencies.repositories import ILoginRepository
from ..user_entity import UserEntity
from ...exceptions import LoginError


class LoginService:

    def __init__(self, repository: ILoginRepository):
        self.repository = repository

    async def check(self,  email: str, password: str):
        login = await self.repository.get(email=email)
        password1 = UserEntity.set_password(password)
        if login is None:
            raise LoginError("invalid or login")
        elif login.password != password1:
            raise LoginError("invalid or password")
        elif not login.active:
            raise LoginError("Подтвердите аккаунт через почту")

        return login
