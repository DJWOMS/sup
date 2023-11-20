from pydantic import BaseModel, constr


class VerifyBase(BaseModel):
    code: constr(max_length=20)
    user_id: int


class CreateVerify(VerifyBase):
    pass
