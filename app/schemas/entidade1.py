from pydantic import BaseModel , Field 
from typing import Annotated

class unidade_saude(BaseModel):
    Cnes: Annotated[int , Field(max_length = 7)]
    tipo_unidade: str |None = None
    veiculos_sus: Annotated[int , Field(max_length = 2)]
