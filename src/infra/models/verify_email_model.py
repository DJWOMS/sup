from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class VerifyEmailModel(Base):
    """Verify email model

    :param id: id записи
    :param code: код подтверждения
    :param user_id: id пользователя
    :param created_at: дата создания
    :param updated_at: дата обновления
    """
    __tablename__ = 'verify_email'

    code: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))



