from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base


class PermissionModel(Base):
    """Модель прав доступа

    :param id: идентификатор
    :param title: название права доступа
    :param code: код права доступа
    :param description: описание прав доступа
    :param users: все юзеры, у которых есть это право доступа
    """

    __tablename__ = "permissions"

    title: Mapped[str] = mapped_column(String(20))
    code: Mapped[int] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(nullable=True)
    users: Mapped[List["UserModel"]] = relationship(
        back_populates="permissions",
        secondary="user_permission",
        lazy="raise_on_sql"
    )
