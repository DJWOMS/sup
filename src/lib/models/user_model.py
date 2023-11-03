from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class  User(Base):
    __tablename__ = 'users'

    name: Mapped[str]
    surname: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    name_telegram: Mapped[str]
    nick_telegram: Mapped[str]
    nick_meet: Mapped[str]
    nick_gitlab: Mapped[str]
    nick_github: Mapped[str]
    role_id: Mapped[str]
