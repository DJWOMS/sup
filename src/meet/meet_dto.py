from datetime import datetime
from pydantic import BaseModel


class MeetBaseDTO(BaseModel):
    title: str
    date: datetime


class UserDTO(BaseModel):
    user_id: int
    color: str = "white"


class CreateMeetDTO(MeetBaseDTO):
    users: list[UserDTO]
