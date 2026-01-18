from pydantic import BaseModel , Field , field_validator , ConfigDict
from typing import Annotated
from uuid import UUID

class Unidade_Saude(BaseModel):
    model_config = ConfigDict(from_attributes = True)

    cnes: str
    nome: str

    @field_validator("cnes")
    @classmethod
    def validar_cnes(cls, v: int) -> int:
        if not v.isdigit():
            raise ValueError("CNES deve conter apenas números")
        if len(v) != 7:
            raise ValueError("CNES deve ter exatamente 7 dígitos")
        return v
