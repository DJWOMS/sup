from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class PermissionModel(Base):
    """Модель прав доступа

    :param id: идентификатор
    :param title: название права доступа
    :param code: код права доступа
    :param description: описание прав доступа
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "permissions"

    title: Mapped[str] = mapped_column(String(20))
    code: Mapped[int] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(nullable=True)
