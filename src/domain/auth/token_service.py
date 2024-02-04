from datetime import datetime, timedelta
from typing import Annotated

import jwt
from fastapi import Depends

from src.app.config.security_config import settings


class TokenService:
    @staticmethod
    def create_access_token(user_id: int, expires_delta: timedelta = None) -> str:
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=settings.access_token_expire_minutes
            )
        to_encode = {"exp": expire, "id": user_id}
        return jwt.encode(
            payload=to_encode,
            key=settings.secret_key,
            algorithm=settings.algorithm
        )


ITokenService = Annotated[TokenService, Depends()]
