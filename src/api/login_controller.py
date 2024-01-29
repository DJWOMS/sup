from fastapi import APIRouter, HTTPException

from src.auth.token_dto import Token
from src.exceptions import LoginError
from ..dependencies.services import ILoginService

router = APIRouter(prefix="/login", tags=["login"])


@router.post("/", response_model=Token)
async def login_user(service: ILoginService, email: str, password: str):
    try:
        return await service.check(email, password)
    except LoginError as e:
        raise HTTPException(status_code=400, detail=str(e))
