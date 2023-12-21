from pydantic import BaseModel, constr


class VerifyBaseDTO(BaseModel):
    code: constr(max_length=20)
    user_id: int


class CreateEmailCodeDTO(VerifyBaseDTO):
    pass


class GetEmailCodeDTO(VerifyBaseDTO):
    pass
