from pydantic import BaseModel, constr


class RoleBase(BaseModel):
    name: constr(max_length=20)
    color: constr(max_length=6)


class CreateRole(RoleBase):
    pass


class UpdateRole(RoleBase):
    pass


class ResponseRole(RoleBase):
    id: int


class ResponseRoleList(RoleBase):
    id: int
