from datetime import date

from sqlalchemy.orm import Mapped

from src.lib.models.base_model import Base


class InvitationModel(Base):
    __tablename__ = 'invitations'

    code: Mapped[str]
    status: Mapped[str]
    at_valid: Mapped[date]
