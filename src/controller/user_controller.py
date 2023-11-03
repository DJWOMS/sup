from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.user_schema import UserSchema
from src.config.database.db_helper import db_helper


router = APIRouter(prefix="/user", tags=["user"])


@router.post("/", response_model=MessageResponse)
def add_message(
        db_session: Session = Depends(db_helper.get_session),
):
    return ReviewService().add(db_session)
