from fastapi import APIRouter , Depends , HTTPException
from app.models.entidade1 import UnidadeSaude
from app.schemas.entidade1 import Unidade_Saude
from sqlalchemy.orm import Session
from app.database import pegar_sessao
from app.core.config import verificar_token
from app.services.entidade_saude import  create_unidade

entidade1 = APIRouter(prefix="/unidade saude" , tags=['unidade saude'])


@entidade1.post("/create")
def create_uni(dados: Unidade_Saude , db: Session = Depends(pegar_sessao), usuario = Depends(verificar_token)):
    return create_unidade(db ,dados)

@entidade1.put("/update/{cnes}", response_model = Unidade_Saude)
def update_unidade(cnes: str , dados: Unidade_Saude , session: Session = Depends(pegar_sessao) , usuario = Depends(verificar_token)):
    unidade = session.query(UnidadeSaude).filter(UnidadeSaude.cnes == cnes).first()
    if not unidade:
        raise HTTPException(status_code = 400 , detail = f"Unidade {cnes} não encontrada")
    unidade.nome = dados.nome
    unidade.cnes = dados.cnes
    session.commit()
    session.refresh(unidade)
    return unidade

@entidade1.get("/lista")
def read_unidade(session: Session = Depends(pegar_sessao) , usuario = Depends(verificar_token)):
    if not usuario:
        raise HTTPException(status_code = 400 , detail="Usuario não autenticado")
    else:
        Unidades = session.query(UnidadeSaude).all()
        return {
            "Unidades": Unidades
        }

@entidade1.delete("/delete/{cnes}")
def delete_unidade(cnes: str , session: Session = Depends(pegar_sessao) , usuario = Depends(verificar_token)):
    unidade = session.query(UnidadeSaude).filter(UnidadeSaude.cnes == cnes).first()
    if not usuario:
        raise HTTPException(status_code = 400 , detail = f"Unidade {cnes} não encontrado !")
    session.delete(unidade)
    session.commit()
    return unidade