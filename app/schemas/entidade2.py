from pydantic import BaseModel , Field , field_validator
from typing import Annotated
from uuid import UUID

# ------- Location -------
class LocationSchemas(BaseModel):
    cod_uf_municipio: int
    regiao_saude: int
    microregiao: int

    @field_validator("cod_uf_municipio")
    @classmethod
    def validar_cod(cls , v: int) -> int:
        if not v.isdigit():
            raise ValueError("Código UF deve conter apenas números")
        if len(v) != 6:
            raise ValueError("Código UF deve conter somente 6 dígitos")
        return v


class LocationCreate(LocationSchemas):
    pass

class LocationResponse(LocationSchemas):
    id: UUID

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


class LeitosCreate(LeitosSchemas):
    pass

class LeitosResponse(LeitosSchemas):
    id: UUID