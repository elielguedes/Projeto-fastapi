from pydantic import BaseModel , Field
from typing import Annotated

class Location(BaseModel):
    cod_uf_municipio: Annotated[int , Field(max_length = 6)]
    regiao_saude: Annotated[int , Field(max_length = 4)]
    microregiao: Annotated[int , Field(max_length = 3)]

class Gestao(BaseModel):
    tipo_gestao: str
    esfera_admin: str
    retencao: str
    

class leitos(BaseModel):
    leitos_tipo_1: int |None = None
    leitos_tipo_2: int |None = None
    leito_tipo_3: int |None = None
    total_leitos: int |None = None
