from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.lib.models.base_model import Base
from src.user.models.user_model import UserModel


class MeetModel(Base):
    __tablename__ = 'meets'

    title: Mapped[str]
    date: Mapped[datetime]
    users: Mapped[list['UserMeetModel']] = relationship('UserMeetModel', lazy='raise_on_sql')
    # users: Mapped[list[UserModel]] = relationship(
    #     UserModel,
    #     secondary="users_meet"
    # )


class UserMeetModel(Base):
    __tablename__ = 'users_meet'

    meet_id: Mapped[int] = mapped_column(ForeignKey('meets.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    color: Mapped[str]
    user: Mapped['UserModel'] = relationship('UserModel', lazy='raise_on_sql')


