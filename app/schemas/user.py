from pydantic import BaseModel , Field , EmailStr , field_validator
from typing import Annotated
from uuid import UUID

class UserBase(BaseModel):
    name: Annotated[str , Field(max_length = 100)]
    email: EmailStr
    perfil: bool

class UserCreate(UserBase):
    senha: Annotated[str , Field(min_length = 1 , max_length = 100)]

class UserResponse(UserBase):
    id: UUID

class MensagemResponse(BaseModel):
    Mensagem: str
