from fastapi import APIRouter, HTTPException

from src.dependencies.services import IEmailService
from src.exceptions import InviteError
from src.email.email_dto import GetEmailCodeDTO

router = APIRouter(prefix="/email")


@router.get("/", response_model=GetEmailCodeDTO)
async def check_email_code(code: str, service: IEmailService):
    try:
        return await service.check_code(code)
    except InviteError as e:
        raise HTTPException(status_code=400, detail=str(e))

