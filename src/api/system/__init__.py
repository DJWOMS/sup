from fastapi.routing import APIRouter

system_routes = APIRouter()


@system_routes.get("/healthcheck")
async def healthcheck():
    return {"health": "OK"}
