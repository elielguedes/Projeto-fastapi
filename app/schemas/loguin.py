from pydantic import BaseModel , Field , EmailStr
from typing import Annotated 
from uuid import UUID

class loguinSchemas(BaseModel):
    email: EmailStr
    senha: Annotated[str , Field(min_length = 1 , max_length = 100)]

class LoguinCreate(loguinSchemas):
    pass
class LoguinResponse(BaseModel):
    id: UUID
    email: EmailStr
