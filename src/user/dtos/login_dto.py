from pydantic import BaseModel, constr


class LoginBase(BaseModel):
    name: constr(max_length=50)
    password: constr(min_length=8)


class CreateLogin(LoginBase):
    pass
