from typing import Annotated
from fastapi import Depends

from src.mit.mit_repository import MitRepository

IMitRepository = Annotated[MitRepository, Depends()]
