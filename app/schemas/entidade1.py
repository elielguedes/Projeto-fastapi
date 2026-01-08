from typing import Annotated
from pydantic import BaseModel , Field 
from uuid import UUID

class unidade_saude_schemas(BaseModel):

    id: Annotated[int , UUID] |None = None
    Cnes: Annotated[str , Field(7)]
    tipo_unidade: Annotated[str , Field(100)]
    veiculos_sus: Annotated[str , Field(100)]