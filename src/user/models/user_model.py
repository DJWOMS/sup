from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.lib.models.base_model import Base


class UserModel(Base):
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
    role_id: Mapped[str] = mapped_column(ForeignKey('role.id'), nullable=True)
