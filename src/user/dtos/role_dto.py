from pydantic import BaseModel, constr


class RoleBaseDTO(BaseModel):
    name: constr(max_length=20)
    color: constr(max_length=6)


class CreateRoleDTO(RoleBaseDTO):
    pass


class GetRoleListDTO(RoleBaseDTO):
    id: int


class GetRoleDTO(RoleBaseDTO):
    id: int


class UpdateRoleDTO(RoleBaseDTO):
    pass
