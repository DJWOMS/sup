from pydantic import BaseModel, EmailStr, constr


class UserBase(BaseModel):
    name: constr(max_length=20)
    surname: constr(max_length=20)
    email: EmailStr
    name_telegram: constr(max_length=50)
    nick_telegram: constr(max_length=50)
    nick_meet: constr(max_length=50)
    nick_gitlab: constr(max_length=50)
    nick_github: constr(max_length=50)
    role_id: int
    right_id: int


class CreateUser(UserBase):
    pass


class UpdateUser(UserBase):
    pass


class UpdatePassword(BaseModel):
    password: str


class ResponseUser(UserBase):
    id: int


class ResponseUserList(UserBase):
    id: int



