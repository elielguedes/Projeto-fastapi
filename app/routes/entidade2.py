from fastapi import APIRouter , Depends , HTTPException
from app.core.config import pegar_sessao , verificar_token
from app.models.entidade2 import Location , Gestao , Leitos
from app.schemas.entidade2 import Gestao , leitos , LocationSchemas
from sqlalchemy.orm import Session

entidade2 = APIRouter(prefix = "/entidade2" , tags=['entidade2'])


@entidade2.get("/listar-location")
def get_location(session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "usuario não autenticado")
    locate = session.query(Location).all()
    return {
        "locate": locate
    }

@entidade2.get("/")
def get_cod_uf(cod_uf: int ,session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    cod = session.query(Location).filter(Location.cod_uf_municipio == cod_uf).first()
    if not user:
        raise HTTPException(status_code = 400 , detail = "Usuario não autenticado")
    session.commit()
    session.refresh(cod)
    return cod
    
@entidade2.put("/entidade2/{id}")
def update(id: str , data: LocationSchemas , session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    cod = session.query(Location).filter(Location.id == id).first()
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    cod.cod_uf_municipio = data.cod_uf_municipio
    cod.regiao_saude = data.regiao_saude
    cod.microregiao = data.microregiao
    session.commit()
    session.refresh(cod)
    return cod

@entidade2.delete("/entidade2/{id}")
def delete(id: int , session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    cod = session.query(Location).filter(Location.id == id).first()
    if not cod:
        raise HTTPException(status_code = 400 , detail = "Registro não encontrado")
    
    session.delete(cod)
    session.commit()
    return cod