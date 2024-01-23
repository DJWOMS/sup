from pydantic import BaseModel, constr, conint


class PermissionBaseDTO(BaseModel):
    title: constr(max_length=20)
    code: conint(ge=0, le=999999)
    description: constr(max_length=300)


class GetPermissionListDTO(PermissionBaseDTO):
    id: int


class CreatePermissionDTO(PermissionBaseDTO):
    pass


class UpdatePermissionDTO(PermissionBaseDTO):
    pass
