from fastapi import APIRouter, HTTPException

from src.auth.token_model import Token
from src.exceptions import LoginError
from src.login.dependencies.services import ILoginService

router = APIRouter(prefix="/login", tags=["login"])


@router.post("/", response_model=Token)
async def login_user(service: ILoginService, email: str, password: str):
    try:
        return await service.check(email, password)
    except LoginError as e:
        raise HTTPException(status_code=400, detail=str(e))
