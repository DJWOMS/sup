from datetime import date

from sqlalchemy.orm import Mapped

from .base_model import Base


class InvitationModel(Base):
    """Invitation model

    :param id: идентификатор
    :param code: код приглашения
    :param status: статус приглашения
    :param at_valid: дата окончания приглашения
    :param created_at: дата создания приглашения
    :param updated_at: дата обновления приглашения
    """
    __tablename__ = "invitations"

    code: Mapped[str]
    # TODO status должен быть Enum
    status: Mapped[str]
    at_valid: Mapped[date]
