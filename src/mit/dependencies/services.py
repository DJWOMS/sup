from typing import Annotated
from fastapi import Depends

from src.mit.mit_service import MitService

IMitService = Annotated[MitService, Depends()]
