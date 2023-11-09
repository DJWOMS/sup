from fastapi import APIRouter

from ..dependencies.services import IRoleService
from src.user.dtos.role_dto import CreateRole

router = APIRouter(prefix="/role", tags=["role"])


@router.post("/")
async def create_role(
    dto: CreateRole,
    service: IRoleService
):
    return await service.create(dto)


