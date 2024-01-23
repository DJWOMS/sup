from fastapi import APIRouter, HTTPException

from src.email.dependencies.services import IEmailService
from src.exceptions import InviteError
from src.email.email__dto import GetEmailCodeDTO

router = APIRouter(prefix="/email", tags=["email"])


@router.get("/", response_model=GetEmailCodeDTO)
async def check_email_code(code: str, service: IEmailService):
    try:
        return await service.check_code(code)
    except InviteError as e:
        raise HTTPException(status_code=400, detail=str(e))

