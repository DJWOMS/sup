from fastapi import APIRouter

from ..dependencies.services import IRightsService
from ..dtos.right_dto import CreateRight, UpdateRight, ResponseRightList

router = APIRouter(prefix="/right", tags=["right"])


@router.post("/", response_model=CreateRight)
async def create_right(dto: CreateRight, service: IRightsService):
    return await service.create(dto)


@router.put("/{pk}", response_model=UpdateRight)
async def update_right(pk: int, dto: UpdateRight, service: IRightsService):
    return await service.update(pk, dto)


@router.delete("/del/{pk}")
async def delete_right(pk: int, service: IRightsService):
    return await service.delete(pk)


@router.get("/get_list", response_model=list[ResponseRightList])
async def get_list_users(service: IRightsService, limit: int = 10):
    return await service.get_list(limit)
