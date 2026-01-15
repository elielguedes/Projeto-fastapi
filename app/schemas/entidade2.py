from pydantic import BaseModel , Field , field_validator
from typing import Annotated
from uuid import UUID

class Location(BaseModel):
    id: Annotated[int , UUID] |None = None
    cod_uf_municipio: Annotated[int , Field(max_length = 6)]
    regiao_saude: Annotated[int , Field(max_length = 4)]
    microregiao: Annotated[int , Field(max_length = 3)]

    @field_validator("cod_uf_municipio")
    @classmethod
    def validar_uf(cls , v: int)-> int:
        if len(v) != 6:
            raise ValueError("UF deve ter exatamente 6 digitos")
        return v 
    
    @field_validator("regiao_saude")
    @classmethod
    def validar_rg(cls , v: int)-> int:
        if len(v) != 4:
            raise ValueError("RG saude precisa ter exatos 4 digitos")
        return v

class Gestao(BaseModel):
    id: UUID
    tipo_gestao: str
    esfera_admin: str
    retencao: str
    

class leitos(BaseModel):
    id: UUID
    leitos_tipo_1: int |None = None
    leitos_tipo_2: int |None = None
    leito_tipo_3: int |None = None
    total_leitos: int |None = None
