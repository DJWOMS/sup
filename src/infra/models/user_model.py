from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class UserModel(Base):
    """Модель пользователя

    :param id: идентификатор
    :param name: имя пользователя
    :param surname: фамилия пользователя
    :param email: email пользователя
    :param password: пароль пользователя
    :param name_telegram: имя в телеграм
    :param nick_telegram: ник в телеграм
    :param nick_google_meet: ник в google meet
    :param nick_gitlab: ник в gitlab
    :param nick_github: ник в github
    :param active: активирован ли пользователь
    :param role_id: роль пользователя
    :param permission_id: права пользователя
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String(20))
    surname: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    password: Mapped[str]
    name_telegram: Mapped[str] = mapped_column(String(50))
    nick_telegram: Mapped[str] = mapped_column(String(50))
    nick_google_meet: Mapped[str] = mapped_column(String(50))
    nick_gitlab: Mapped[str] = mapped_column(String(50))
    nick_github: Mapped[str] = mapped_column(String(50))
    is_active: Mapped[bool] = mapped_column(default=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))
    permission_id: Mapped[int] = mapped_column(ForeignKey("permissions.id"))
