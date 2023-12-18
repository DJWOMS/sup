from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.lib.models.base_model import Base


class MeetModel(Base):
    __tablename__ = 'meets'

    title: Mapped[str]
    date: Mapped[datetime]


class UserMeetModel(Base):
    __tablename__ = 'users_meet'

    meet_id: Mapped[int] = mapped_column(ForeignKey('meets.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    color: Mapped[str]

