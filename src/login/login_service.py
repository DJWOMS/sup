from datetime import timedelta

from src.auth.token_service import ITokenService
from src.auth.token_model import Token
from src.login.dependencies.repositories import ILoginRepository
from src.user.user_entity import UserEntity
from src.config.project_config import settings
from src.exceptions import LoginError


class LoginService:

    def __init__(self, repository: ILoginRepository, token_service: ITokenService):
        self.repository = repository
        self.token_service = token_service

    async def check(self,  email: str, password: str) -> Token:
        user = await self.repository.get(email=email)
        password1 = UserEntity.set_password(password)
        if user is None:
            raise LoginError("invalid or login")
        elif user.password != password1:
            raise LoginError("invalid or password")
        elif not user.active:
            raise LoginError("Подтвердите аккаунт через почту")

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = Token(access_token=self.token_service.create_access_token(
            user.id, expires_delta=access_token_expires,
            )
        )
        return access_token
