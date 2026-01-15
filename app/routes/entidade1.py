from fastapi import APIRouter , Depends
from app.models.entidade1 import UnidadeSaude
from app.schemas.entidade1 import UnidadeSaude
from app.core.security import oauth2_schemas 
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import pegar_sessao
from app.core.config import verificar_token
from app.services.entidade_saude import  create_unidade

entidade1 = APIRouter()


@entidade1.post("/")
def create_uni(dados: UnidadeSaude , db: Session = Depends(pegar_sessao), usuario = Depends(verificar_token)):
    return create_unidade(db ,dados)