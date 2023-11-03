from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Базовая модель SqlAlchemy
    """

    __abstarct__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
