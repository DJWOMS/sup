from pydantic import BaseModel, constr


class LoginBaseDTO(BaseModel):
    name: constr(max_length=50)
    password: constr(min_length=8)


class CreateLoginDTO(LoginBaseDTO):
    pass
