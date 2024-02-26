from ..models.user_meet_model import UserMeetModel

from ...domain.meet.meet_dto import UserMeetDTO

class UserMeetRepository:
    def __init__(self, session):
        self.session = session


    async def create(self, dto: list[UserMeetDTO], meet_id: int):
        _users = []
        for user in dto:
            _user = UserMeetModel(meet_id=meet_id, user_id=user.user_id, color=user.color)
            _users.append(_user)
        self.session.add_all([*_users])
        await self.session.commit()
        return _users

    async def get(self, meet_id: int):
        return await self.session.query(UserMeetModel).filter_by(meet_id=meet_id).all()
