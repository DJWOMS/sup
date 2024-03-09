from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from .base_model import Base


class UserPermissionModel(Base):
    """ Модель разрешений пользователя

    :param id: идентификатор
    :param user_id: id пользователя
    :param permission_id: id разрешения
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "user_permission"
    user_id: Mapped[int] = mapped_column(ForeignKey(
        "users.id",
        ondelete="CASCADE",
    ),
        primary_key=True
    )
    permission_id: Mapped[int] = mapped_column(ForeignKey(
        "permissions.id",
        ondelete="CASCADE",
    ),
        primary_key=True
    )
