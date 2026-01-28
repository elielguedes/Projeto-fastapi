from pydantic import BaseModel , Field , field_validator , model_validator
from ..models.entidade2 import Location
from typing import Annotated
from uuid import UUID

# ------- Location -------
class LocationSchemas(BaseModel):
    cod_uf_municipio: int
    regiao_saude: int
    microregiao: int

class LocationCreate(LocationSchemas):
    pass

class LocationResponse(BaseModel):
    id: UUID
    cod_uf_municipio: int |None = None
    regiao_saude: int |None = None
    microregiao: int |None = None

# --------Getão -------
class GestaoSchemas(BaseModel):
    tipo_gestao: str
    esfera_admin: str
    retencao: str

class GestaoCreate(GestaoSchemas):
    pass

class GestaoResponse(GestaoSchemas):
    id: UUID

# ------ Leitos -------
class LeitosSchemas(BaseModel):
    leitos_tipo_1: int |None = None
    leitos_tipo_2: int |None = None
    leitos_tipo_3: int |None = None
    total_leitos: int |None = None

    @model_validator(mode = "after")
    def calcular_leitos(self):
        self.total_leitos = (self.leitos_tipo_1 or 0) + (self.leitos_tipo_2 or 0) + (self.leitos_tipo_3 or 0)
        return self
        
class LeitosCreate(LeitosSchemas):
    pass

class LeitosResponse(LeitosSchemas):
    id: UUID