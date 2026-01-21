from fastapi import APIRouter , Depends , HTTPException
from ..models.entidade1 import UnidadeSaude
from ..schemas.entidade1 import UnidadeCreator
from sqlalchemy.orm import Session
from ..database import pegar_sessao
from ..core.config import verificar_token
from ..services.entidade_saude import  create_unidade

entidade1 = APIRouter(prefix="/unidade-saude" , tags=['unidade-saude'])


@entidade1.post("/create")
def create_uni(dados: UnidadeCreator , db: Session = Depends(pegar_sessao), usuario = Depends(verificar_token)):
    return create_unidade(db ,dados)

@entidade1.put("/update/{cnes}", response_model = UnidadeCreator)
def update_unidade(cnes: str , dados: UnidadeCreator , session: Session = Depends(pegar_sessao) , usuario = Depends(verificar_token)):
    if not usuario:
        raise HTTPException(status_code = 400 , detail = "User not authticator")
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