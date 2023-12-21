from fastapi import APIRouter, HTTPException

from ..dependencies.services import ILoginService
from ..dtos.login_dto import CreateLoginDTO
from ...exceptions import LoginError

router = APIRouter(prefix="/login", tags=["login"])


@router.post("/", response_model=CreateLoginDTO)
async def login_user(email: str, password: str, service: ILoginService):
    try:
        return await service.check(email, password)
    except LoginError as e:
        raise HTTPException(status_code=400, detail=str(e))
