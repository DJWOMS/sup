from datetime import datetime
from pydantic import BaseModel


class MeetBase(BaseModel):
    meet_title: str
    date: datetime


class UserMeet(BaseModel):
    user_id: int
    color: str = "white"


class CreateUserMeet(MeetBase):
    users: list[UserMeet]
