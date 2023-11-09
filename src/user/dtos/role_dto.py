from pydantic import BaseModel, EmailStr, ConfigDict, model_validator


class RoleBase(BaseModel):
    name: str
    color: str


class CreateRole(RoleBase):
    pass
