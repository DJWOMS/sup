from fastapi import APIRouter, HTTPException

from src.app.dependencies.services import IEmailService
from src.lib.exceptions import InviteError
from src.domain.email.email_dto import GetEmailCodeDTO


router = APIRouter(prefix="/email", tags=["email"])


@router.get("/", response_model=GetEmailCodeDTO)
async def check_email_code(code: str, service: IEmailService):
    try:
        return await service.check_code(code)
    except InviteError as e:
        raise HTTPException(status_code=400, detail=str(e))

