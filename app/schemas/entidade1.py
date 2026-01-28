from pydantic import BaseModel , Field , field_validator , ConfigDict
from typing import Annotated
from uuid import UUID


class UnidadeBase(BaseModel):
    nome: str

class Unidade_Saude(UnidadeBase):
    cnes: Annotated[str , Field(max_length = 7)]

    @field_validator("cnes")
    @classmethod
    def validar_cnes(cls , v: str)-> str:
        if not v.isdigit():
            raise ValueError("Cnes deve conter apenas números")
        return v

class UnidadeUpdate(UnidadeBase):
    pass

class UnidadeCreator(Unidade_Saude):
    pass

class UnidadeResponse(Unidade_Saude):
    id: UUID
    cnes: str

class MensagemRespose(BaseModel):
    mensagem: str