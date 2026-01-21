from pydantic import BaseModel , Field , field_validator , ConfigDict
from typing import Annotated
from uuid import UUID

class Unidade_Saude(BaseModel):
    cnes: Annotated[str , Field(max_length = 100)]
    nome: str

    @field_validator("cnes")
    @classmethod
    def validar_cnes(cls, v: int) -> int:
        if not v.isdigit():
            raise ValueError("CNES deve conter apenas números")
        if len(v) != 7:
            raise ValueError("CNES deve ter exatamente 7 dígitos")
        return v
class UnidadeCreator(Unidade_Saude):
    pass

class UnidadeResponse(BaseModel):
    id: UUID
