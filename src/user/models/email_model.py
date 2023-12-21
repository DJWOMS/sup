from sqlalchemy.orm import Mapped

from src.lib.models.base_model import Base


class VerifyEmailModel(Base):
    __tablename__ = 'verify_email'

    code: Mapped[str]
    user_id: Mapped[int]



