from fastapi import HTTPException
from ..models import UnidadeSaude
from sqlalchemy.orm import Session
from ..schemas.entidade1 import UnidadeCreator

def create_unidade(db: Session , unidade: UnidadeCreator):
    if not unidade.cnes:
        raise HTTPException(status_code = 400 , detail = "CNES Invalido")
    db_unidade = UnidadeSaude(cnes = unidade.cnes ,nome = unidade.nome)
    db.add(db_unidade)
    db.commit()
    db.refresh(db_unidade)
    return db_unidade

def update_unidade_service(cnes: str , session: Session , dados: UnidadeCreator):
    unidade = session.query(UnidadeSaude).filter(UnidadeSaude.cnes == cnes).first()
    if not unidade:
        raise HTTPException(status_code = 404 , detail = f"Unidade {cnes} não encontrada")
    unidade.nome = dados.nome

    session.commit()
    session.refresh(unidade)
    return unidade

def delete_unidade_service(session: Session , cnes: str):
    unidade = session.query(UnidadeSaude).filter(UnidadeSaude.cnes == cnes).first()
    if not unidade:
        raise HTTPException(status_code = 400 , detail = "CNES não encontrado")
    session.delete(unidade)
    session.commit()
    return unidade