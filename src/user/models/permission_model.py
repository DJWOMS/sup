from sqlalchemy.orm import Mapped

from src.lib.models.base_model import Base


class PermissionModel(Base):
    __tablename__ = 'permissions'

    title: Mapped[str]
    code: Mapped[int]
    description: Mapped[str]
