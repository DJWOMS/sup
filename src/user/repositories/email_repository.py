from ..dependencies.session import ISession
from ..dtos.email__dto import CreateVerify
from ..models.email_model import VerifyEmailModel


class EmailRepository:

    def __init__(self, session: ISession):
        self.session = session

    async def create(self, dto: CreateVerify):
        instance = VerifyEmailModel(**dto.model_dump())
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        print(f"https://127.0.0.1:8000/verify/{instance.code}")
        return instance

