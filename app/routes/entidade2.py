from fastapi import APIRouter , Depends , HTTPException
from ..core.config import pegar_sessao , verificar_token
from ..models.entidade2 import Location , Gestao , Leitos
from ..schemas.entidade2 import LeitosCreate , LocationCreate , GestaoCreate
from ..schemas.entidade2 import LeitosResponse , LocationResponse , GestaoResponse
from sqlalchemy.orm import Session
from ..services.entidade_service import get_service_uf , update_id_lct , delete_service_lct , update_service_gse , delete_service_gse , put_service_leitos ,delete_service_leitos

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
async def get_cod_uf(cod_uf: int ,session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "Usuario não autenticado")
    return get_service_uf(session , cod_uf)
    
@entidade2.put("/entidade2/{id}", response_model = LocationResponse)
async def update(id: str , dados: LocationCreate , session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    return update_id_lct(id , session ,dados)

@entidade2.delete("/delete_location/{id}")
async def delete(id: str , session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    return delete_service_lct(id , session)
# ===== Gestao =====
@entidade2.get("/gestao")
async def get_gestao(session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "Usuario não autenticado")
    gse = session.query(Gestao).all()
    return gse

@entidade2.get("/gestao/{id}")
async def get_gestao_id(id: str , session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    gse_id = session.query(Gestao).filter(Gestao.id == id).first()
    if not gse_id:
        raise HTTPException(status_code = 400 , detail = "Cadastro não encontrado")
    return gse_id

@entidade2.get("/gestao")
async def gse_tipo_gse(tipo_gse: str , session: Session = Depends(pegar_sessao) , user: Session = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    gse_tipo_gse = session.query(Gestao).filter(Gestao.tipo_gestao == tipo_gse).first()
    return {
        "ges_tipo_ges": gse_tipo_gse
    }

@entidade2.put("/gestao_update", response_model = GestaoResponse)
async def update_gse(id: str , data: GestaoCreate , session: Session = Depends(pegar_sessao) , user: Session = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    return update_service_gse(id , data , session)

@entidade2.delete("/Gestao_delete/{id}")
async def delete_gse(id: str , session: Session = Depends(pegar_sessao) , user: Session = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    return delete_service_gse(id , session)
# ===== Leitos =====
@entidade2.get("/leitos")
async def get_leitos(session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    leitos = session.query(Leitos).all()
    return {
        "leitos": leitos
    }

@entidade2.get("/leitos/{id}")
async def get_leitos_id(id: str , session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    leitos = session.query(Leitos).filter(Leitos.id == id).first()
    if not leitos:
        raise HTTPException(status_code = 400 , detail = "Cadastro não encontrado")
    return leitos

@entidade2.put("/update_leitos/{id}", response_model = LeitosResponse)
async def update_get_leitos(id: str , data: LeitosCreate , session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "user not autheticator")
    return put_service_leitos(id , data , session)

@entidade2.delete("/delete_leitos/{id}")
async def delete_leitos(id: str , session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autheticator")
    return delete_service_leitos(id , session)