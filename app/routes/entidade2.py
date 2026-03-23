from fastapi import APIRouter , Depends , HTTPException
from ..core.config import pegar_sessao , verificar_token
from ..models.entidade2 import Location , Gestao , Leitos
from ..schemas.entidade2 import LeitosCreate , LocationCreate , GestaoCreate
from ..schemas.entidade2 import LeitosResponse ,  GestaoResponse , LocationResponse
from sqlalchemy.orm import Session
from ..repositoryes.entidade2 import EntidadeRepositoryes
from ..services.entidade_service import EntidadeService

entidade2 = APIRouter(prefix = "/entidade2" , tags=['entidade2'])

# ===== Location =====

@entidade2.get("/listar-location")
async def get_location(session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "usuario não autenticado")
    locate = session.query(Location).all()
    return {
        "locate": locate
    }

@entidade2.get("/Location")
async def get_cod_uf(cod_uf: int ,db: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "Usuario não autenticado")
    repository = EntidadeRepositoryes(db)
    service = EntidadeService(repository)
    return service.get_service_uf(cod_uf)
    
@entidade2.put("/entidade2/{id}", response_model = LocationResponse)
async def update(id: str , dados: LocationCreate , db: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    repository = EntidadeRepositoryes(db)
    service = EntidadeService(repository)
    return service.update_id_lct(dados , id)

@entidade2.delete("/delete_location/{id}", response_model = LocationResponse)
async def delete(id: str , db: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    repository = EntidadeRepositoryes(db)
    service = EntidadeService(repository)
    return service.delete_service_lct(id , db)

# ===== Gestao =====
@entidade2.get("/gestao/get")
async def get_gestao(db: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "Usuario não autenticado")
    repository = EntidadeRepositoryes(db)
    return repository.get_by_gestao()

@entidade2.get("/gestao/{id}", response_model = GestaoResponse)
async def get_gestao_id(id: str , db: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    repository = EntidadeRepositoryes(db)
    return repository.get_by_id(id)

@entidade2.get("/gestao" , response_model = GestaoResponse)
async def gse_tipo_gse(tipo_gse: str , db: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    repository = EntidadeRepositoryes(db)
    gse_tipo_gse = repository.get_by_tipo(tipo_gse)
    return gse_tipo_gse

@entidade2.put("/gestao_update", response_model = GestaoResponse)
async def update_gse(id: str , data: GestaoCreate , db: Session = Depends(pegar_sessao) , user: Session = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    repository = EntidadeRepositoryes(db)
    service = EntidadeService(repository)
    return service.update_service_gse(data , id)

@entidade2.delete("/Gestao_delete/{id}" , response_model = GestaoResponse)
async def delete_gse(id: str , db: Session = Depends(pegar_sessao) , user: Session = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    repository = EntidadeRepositoryes(db)
    service = EntidadeService(repository)
    return service.delete_service_gse(id)

# ===== Leitos =====

@entidade2.get("/leitos")
async def get_leitos(db: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    repository = EntidadeRepositoryes(db)
    leitos = repository.get()
    return leitos

@entidade2.get("/leitos/{id}" , response_model = LeitosResponse)
async def get_leitos_id(id: str , db: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    repository = EntidadeRepositoryes(db)
    leitos = repository.get_by_leito(id)
    if not leitos:
        raise HTTPException(status_code = 400 , detail = "Cadastro não encontrado")
    return leitos

@entidade2.put("/update_leitos/{id}", response_model = LeitosResponse)
async def update_get_leitos(id: str , data: LeitosCreate , db: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "user not autheticator")
    repository = EntidadeRepositoryes(db)
    service = EntidadeService(repository)
    return service.put_service_leitos(id , data)


@entidade2.delete("/delete_leitos/{id}" , response_model = LeitosResponse)
async def delete_leitos(id: str , db: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autheticator")
    repository = EntidadeRepositoryes(db)
    service = EntidadeService(repository)
    return service.delete_service_leitos(id)
