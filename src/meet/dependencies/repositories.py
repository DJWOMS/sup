from typing import Annotated
from fastapi import Depends

from src.meet.meet_repository import MeetRepository

IMeetRepository = Annotated[MeetRepository, Depends()]
