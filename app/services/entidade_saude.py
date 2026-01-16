from fastapi import HTTPException
from app.models import UnidadeSaude
from sqlalchemy.orm import Session
from app.schemas.entidade1 import Unidade_Saude

def create_unidade(db: Session , Unidade: Unidade_Saude):
    if not Unidade.cnes:
        raise HTTPException(status_code = 400 , detail = "CNES Invalido")
    db_unidade = UnidadeSaude(cnes = Unidade.cnes ,nome = Unidade.nome)
    db.add(db_unidade)
    db.commit()
    db.refresh(db_unidade)
    return db_unidade

