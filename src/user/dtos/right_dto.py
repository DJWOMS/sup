from pydantic import BaseModel, constr, conint


class RightBase(BaseModel):
    title: constr(max_length=20)
    code: conint(ge=0, le=999999)
    description: constr(max_length=300)


class CreateRight(RightBase):
    pass


class UpdateRight(RightBase):
    pass


class ResponseRightList(RightBase):
    id: int
