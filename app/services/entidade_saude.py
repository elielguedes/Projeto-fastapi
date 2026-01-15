from fastapi import HTTPException
from app.models import UnidadeSaude
from sqlalchemy.orm import Session

def create_unidade(db: Session , Unidade: UnidadeSaude):
    if not Unidade.cnes:
        raise HTTPException(status_code = 400 , detail = "CNES Invalido")
    db_unidade = UnidadeSaude(cnes = Unidade.cnes)
    db.add(db_unidade)
    db.commit()
    db.refresh(db_unidade)
    return db_unidade