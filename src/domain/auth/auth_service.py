import jwt

from typing import Annotated

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from pydantic import ValidationError

from src.app.config.security_config import settings

from src.app.dependencies.repositories import IUserRepository

from src.domain.auth.auth_dto import TokenPayload
from src.domain.user.user_dto import GetUserDTO

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/v1/login/access-token"
)

# TODO: это бы убрать в депенденсис
TokenDep = Annotated[str, Depends(reusable_oauth2)]


class AuthService:

    async def __call__(self, repository: IUserRepository, token: TokenDep):
        try:
            payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
            token_data = TokenPayload(**payload)
        except (jwt.PyJWTError, ValidationError):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")
        user = await repository.get(token_data.id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        if not user.active:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
        return user


# TODO: это тоже бы убрать в депенденсис
CurrentUser = Annotated[GetUserDTO, Depends(AuthService())]
