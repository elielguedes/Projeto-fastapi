from fastapi import HTTPException
from ..models.entidade1 import UnidadeSaude
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

def delete_unidade_service(cnes: str , db: Session):
    unidade = db.query(UnidadeSaude).filter(UnidadeSaude.cnes == cnes).first()
    if not unidade:
        raise HTTPException(status_code = 400 , detail = "CNES não encontrado")
    db.delete(unidade)
    db.commit()
    return {"mensagem": "Unidade {cnes} removida com sucesso"}