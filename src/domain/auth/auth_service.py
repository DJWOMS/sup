import jwt
from typing import Annotated

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError

from src.app.dependencies.repositories import IUserRepository
from src.app.config.project_config import settings
from src.domain.auth.auth_dto import TokenPayload

from src.domain.user.user_dto import GetUserDTO
from src.domain.auth.token_service import ALGORITHM

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


TokenDep = Annotated[str, Depends(reusable_oauth2)]


class AuthService:

    async def __call__(self, repository: IUserRepository, token: TokenDep):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
            token_data = TokenPayload(**payload)
        except (jwt.PyJWTError, ValidationError):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")
        user = await repository.get(token_data.id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not user.active:
            raise HTTPException(status_code=400, detail="Inactive user")
        return user


CurrentUser = Annotated[GetUserDTO, Depends(AuthService())]

