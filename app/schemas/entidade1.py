from pydantic import BaseModel , Field , field_validator
from typing import Annotated
from uuid import UUID

class unidade_saude(BaseModel):
    id: Annotated[int , UUID] |None = None
    Cnes: Annotated[str , Field(max_length = 7)]
    tipo_unidade: str |None = None
    veiculos_sus: Annotated[int , Field(max_length = 2)]

    @field_validator("Cnes")
    @classmethod
    def validar_Cnes(cls , v: str)-> str:
        if not v.isdigit():
            raise ValueError("CNES deve conter apenas números")
        if len(v) != 7:
            raise ValueError("CNES deve ter exatamentw 7 digitos")
        return v
    