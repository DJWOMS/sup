from datetime import datetime

from sqlalchemy.orm import Mapped

from src.lib.models.base_model import Base


class UserMeetModel(Base):
    __tablename__ = 'user_mit'

    meet_title: Mapped[str]
    date: Mapped[datetime]
    user_id: Mapped[int]
    color: Mapped[str]
