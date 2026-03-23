from fastapi import APIRouter , Depends , HTTPException
from ..models.entidade1 import UnidadeSaude
from ..schemas.entidade1 import UnidadeCreator , UnidadeUpdate , UnidadeResponse , MensagemRespose
from sqlalchemy.orm import Session
from ..database import pegar_sessao
from ..core.config import verificar_token
from ..services.entidade_saude import  SaudeService
from ..repositoryes.entidade1 import SaudeRepository
from ..pipeline.pipeline import run_pipeline

entidade1 = APIRouter(prefix="/unidade-saude" , tags=['unidade-saude'])

@entidade1.post("/create" , response_model = UnidadeResponse)
def create_uni(dados: UnidadeCreator , db: Session = Depends(pegar_sessao), usuario = Depends(verificar_token)):
    if not usuario:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    repository = SaudeRepository(db)
    service = SaudeService(repository)
    return service.create_unidade(dados)

@entidade1.put("/update/{cnes}", response_model = UnidadeUpdate)
def update_cnes(cnes: str , dados: UnidadeUpdate , db: Session = Depends(pegar_sessao) , usuario = Depends(verificar_token)):
    if not usuario:
        raise HTTPException(status_code = 400 , detail = "User not authticator")
    repository = SaudeRepository(db)
    service = SaudeService(repository)
    return service.update_unidade_service(cnes , dados)

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
def delete_unidade(cnes: str , db: Session = Depends(pegar_sessao) , usuario = Depends(verificar_token)):
    if not usuario:
        raise HTTPException(status_code = 400 , detail = "User not autheticator")
    repository = SaudeRepository(db)
    service = SaudeService(repository)
    return service.delete_unidade_service(cnes , db)