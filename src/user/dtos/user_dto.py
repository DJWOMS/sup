from pydantic import BaseModel, EmailStr, constr


class UserBaseDTO(BaseModel):
    name: constr(max_length=20)
    surname: constr(max_length=20)
    email: EmailStr
    name_telegram: constr(max_length=50)
    nick_telegram: constr(max_length=50)
    nick_google_meet: constr(max_length=50)
    nick_gitlab: constr(max_length=50)
    nick_github: constr(max_length=50)
    role_id: int
    permission_id: int


class CreateUserDTO(UserBaseDTO):
    pass


class GetUserListDTO(UserBaseDTO):
    id: int


class GetUserDTO(UserBaseDTO):
    id: int


class UpdateUserDTO(UserBaseDTO):
    pass


class UpdatePasswordDTO(BaseModel):
    password: str
