from pydantic import BaseModel , Field , EmailStr
from typing import Annotated
from uuid import UUID

class user(BaseModel):

    name: Annotated[str , Field(max_length = 100)]
    email: EmailStr
    senha: Annotated[str , Field(min_length = 1 , max_length = 100)]
    perfil: bool

class loguinSchemas(BaseModel):
    email: EmailStr
    senha: Annotated[str , Field(min_length = 1 , max_length = 100)]
