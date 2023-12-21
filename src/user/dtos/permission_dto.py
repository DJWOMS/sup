from pydantic import BaseModel, constr, conint


class PermissionBase(BaseModel):
    title: constr(max_length=20)
    code: conint(ge=0, le=999999)
    description: constr(max_length=300)


class CreatePermissionDTO(PermissionBase):
    pass


class UpdatePermissionDTO(PermissionBase):
    pass


class ResponsePermissionListDTO(PermissionBase):
    id: int
