from datetime import datetime

from sqlalchemy.orm import Mapped, relationship
from .base_model import Base


class MeetModel(Base):
    """Модель митапа

    :param id: идентификатор
    :param title: название митапа
    :param date: дата митапа
    :param color: цвет митапа
    :param users: пользователи, участвующие в митапе
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "meets"

    title: Mapped[str]
    date: Mapped[datetime]
    color: Mapped[str]
    users: Mapped[list["UserModel"]] = relationship(
        back_populates="meets",
        secondary="users_meet",
        lazy="raise_on_sql"
    )
