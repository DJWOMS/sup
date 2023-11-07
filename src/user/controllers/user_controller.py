from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.config.database.db_helper import db_helper
from src.user.servises.user_servise import UserService
from src.user.schema.user_schema import CreateUser

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/")
async def create_user(
        data: CreateUser,
        db_session: Session = Depends(db_helper.get_session),
):
    return await UserService().create(data, db_session)
