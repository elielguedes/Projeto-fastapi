from pydantic import BaseModel , Field , EmailStr
from typing import Annotated
from uuid import UUID

class Users(BaseModel):

    id: Annotated[int , UUID]|None = None
    name: Annotated[str , Field(max_length = 100)]
    email: EmailStr
    perfil: bool

