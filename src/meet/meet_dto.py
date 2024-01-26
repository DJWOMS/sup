from datetime import datetime
from pydantic import BaseModel


class MeetBaseDTO(BaseModel):
    title: str
    date: datetime


class UserMeetDTO(BaseModel):
    user_id: int
    color: str = "white"


class CreateMeetDTO(MeetBaseDTO):
    users: list[UserMeetDTO]


class UpdateMeetDTO(CreateMeetDTO):
    pass


class MeetDTO(MeetBaseDTO):
    id: int


class UserMeetResponseDTO(BaseModel):
    id: int
    name: str
    name_telegram: str
    nick_telegram: str
    color: str = "white"

    class Config:
        from_attributes = True


class MeetResponseDTO(MeetBaseDTO):
    id: int
    users: list[UserMeetResponseDTO] | None = None

    class Config:
        from_attributes = True


