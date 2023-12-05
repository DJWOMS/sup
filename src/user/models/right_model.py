from sqlalchemy.orm import Mapped

from src.lib.models.base_model import Base


class RightModel(Base):
    __tablename__ = 'right'

    title: Mapped[str]
    code: Mapped[int]
    description: Mapped[str]
