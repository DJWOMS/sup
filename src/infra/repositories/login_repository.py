from sqlalchemy import select

from ..database.session import ISession
from ..models.user_model import UserModel


class LoginRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def get(self, email: str):
        stmt = select(UserModel).filter_by(email=email)
        raw = await self.session.execute(stmt)
        return raw.scalar_one_or_none()
