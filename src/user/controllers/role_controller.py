from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.config.database.db_helper import db_helper
from src.user.servises.role_servise import RoleService
from src.user.schema.role_schema import CreateRole

router = APIRouter(prefix="/role", tags=["role"])


@router.post("/")
async def create_role(
        data: CreateRole,
        db_session: Session = Depends(db_helper.get_session),
):
    return await RoleService().create(data, db_session)
