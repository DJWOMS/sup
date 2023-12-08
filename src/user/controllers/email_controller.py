from fastapi import APIRouter, HTTPException

from src.exceptions import InviteError
from src.user.dependencies.services import IEmailService
from src.user.dtos.email__dto import CheckEmail

router = APIRouter(prefix="/email", tags=["email"])


@router.get("/", response_model=CheckEmail)
async def check_code_email(code: str, service: IEmailService):
    try:
        return await service.check(code)
    except InviteError as e:
        raise HTTPException(status_code=400, detail=str(e))

