from datetime import datetime
from pydantic import BaseModel


class MeetDTO(BaseModel):
    title: str
    date: datetime


class UserMeetDTO(BaseModel):
    user_id: int
    color: str = "white"


class CreateMeetDTO(MeetDTO):
    users: list[UserMeetDTO]


class UserMeetResponseDTO(BaseModel):
    id: int
    name: str
    name_telegram: str
    nick_telegram: str
    color: str = "white"

    class Config:
        from_attributes = True


class MeetResponseDTO(MeetDTO):
    id: int
    users: list[UserMeetResponseDTO]

    class Config:
        from_attributes = True


