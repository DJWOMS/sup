from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base


class UserMeetModel(Base):
    """Модель пользователя в митапе

    :param id: идентификатор
    :param meet_id: id митапа
    :param user_id: id пользователя
    :param color: цветовой индикатор посещения митапа
    :param user: связь с пользователем
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "users_meet"

    meet_id: Mapped[int] = mapped_column(ForeignKey("meets.id", ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    color: Mapped[str]
    #Сделать Enum
    status: Mapped[str]

