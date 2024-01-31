from typing import Union

from pydantic import BaseModel


class TokenPayload(BaseModel):
    id: Union[int, None] = None
