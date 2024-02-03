from datetime import datetime, timedelta
from typing import Annotated

import jwt
from fastapi import Depends

from src.app.config.project_config import settings

ALGORITHM = "HS256"


class TokenService:

    def create_access_token(self, user_id: int, expires_delta: timedelta = None) -> str:
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        to_encode = {"exp": expire, "id": user_id}
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt


ITokenService = Annotated[TokenService, Depends()]
