from pydantic import BaseModel , Field , field_validator
from typing import Annotated
from uuid import UUID

class LocationSchemas(BaseModel):
    cod_uf_municipio: int
    regiao_saude: int
    microregiao: int

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
