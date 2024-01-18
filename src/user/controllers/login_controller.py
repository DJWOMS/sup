from fastapi import APIRouter, HTTPException

from ..dependencies.services import ILoginService
from src.user.auth.token_model import Token
from ...exceptions import LoginError

router = APIRouter(prefix="/login", tags=["login"])


@router.post("/", response_model=Token)
async def login_user(service: ILoginService, email: str, password: str):
    try:
        return await service.check(email, password)
    except LoginError as e:
        raise HTTPException(status_code=400, detail=str(e))
