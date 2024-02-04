from sqlalchemy.orm import Mapped

from .base_model import Base


class RoleModel(Base):
    """Модель роли

    :param id: идентификатор
    :param name: название роли
    :param color: цвет роли
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = "roles"

    name: Mapped[str]
    color: Mapped[str]
