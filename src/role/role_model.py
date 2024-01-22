from sqlalchemy.orm import Mapped

from src.lib.models.base_model import Base


class RoleModel(Base):
    __tablename__ = 'role'

    name: Mapped[str]
    color: Mapped[str]

