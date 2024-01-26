from typing import Annotated
from fastapi import Depends

from src.login.login_repository import LoginRepository


ILoginRepository = Annotated[LoginRepository, Depends()]

