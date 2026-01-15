from pydantic import BaseModel , Field , field_validator
from typing import Annotated
from uuid import UUID

class UnidadeSaude(BaseModel):
    id: int | None = None
    cnes: str = Field(max_length=7)
    tipo_unidade: str | None = None
    veiculos_sus: int = Field(ge=0, le=99)

    @field_validator("cnes")
    @classmethod
    def validar_cnes(cls, v: str) -> str:
        if not v.isdigit():
            raise ValueError("CNES deve conter apenas números")
        if len(v) != 7:
            raise ValueError("CNES deve ter exatamente 7 dígitos")
        return v
