from pydantic import BaseModel


class BaseDto(BaseModel):
    """Базовая схема Pydantic"""
    class Config:
        from_attributes = True
