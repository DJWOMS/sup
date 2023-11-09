from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str
    color: str


class CreateRole(RoleBase):
    pass


class ResponseRole(RoleBase):
    id: int


class ResponseRoleList(RoleBase):
    id: int

