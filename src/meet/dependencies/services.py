from typing import Annotated
from fastapi import Depends

from src.meet.meet_service import MeetService

IMeetService = Annotated[MeetService, Depends()]
