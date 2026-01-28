from fastapi import APIRouter , Depends , HTTPException
from ..models.entidade1 import UnidadeSaude
from ..schemas.entidade1 import UnidadeCreator , UnidadeUpdate , UnidadeResponse , MensagemRespose
from sqlalchemy.orm import Session
from ..database import pegar_sessao
from ..core.config import verificar_token
from ..services.entidade_saude import  create_unidade , update_unidade_service , delete_unidade_service

entidade1 = APIRouter(prefix="/unidade-saude" , tags=['unidade-saude'])

@entidade1.post("/create" , response_model = UnidadeResponse)
def create_uni(dados: UnidadeCreator , db: Session = Depends(pegar_sessao), usuario = Depends(verificar_token)):
    if not usuario:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    return create_unidade(db ,dados)

@entidade1.put("/update/{cnes}", response_model = UnidadeUpdate)
def update_cnes(cnes: str , dados: UnidadeUpdate , session: Session = Depends(pegar_sessao) , usuario = Depends(verificar_token)):
    if not usuario:
        raise HTTPException(status_code = 400 , detail = "User not authticator")
    return update_unidade_service(cnes, session , dados)


@entidade1.get("/lista")
def read_unidade(session: Session = Depends(pegar_sessao) , usuario = Depends(verificar_token)):
    if not usuario:
        raise HTTPException(status_code = 400 , detail="Usuario não autenticado")
    else:
        Unidades = session.query(UnidadeSaude).all()
        return {
            "Unidades": Unidades
        }

@entidade1.delete("/delete/{cnes}" , response_model = MensagemRespose)
def delete_unidade(cnes: str , session: Session = Depends(pegar_sessao) , usuario = Depends(verificar_token)):
    if not usuario:
        raise HTTPException(status_code = 400 , detail = "User not autheticator")
    return delete_unidade_service(cnes , session)
    