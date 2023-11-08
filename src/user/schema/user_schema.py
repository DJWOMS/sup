from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    surname: str
    email: EmailStr
    name_telegram: str
    nick_telegram: str
    nick_meet: str
    nick_gitlab: str
    nick_github: str
    role_id: int


class CreateUser(UserBase):
    pass
