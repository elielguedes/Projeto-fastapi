from fastapi import APIRouter , Depends , HTTPException
from ..core.config import pegar_sessao , verificar_token
from ..models.entidade2 import Location , Gestao , Leitos
from ..schemas.entidade2 import LeitosCreate , LocationCreate , GestaoCreate
from ..schemas.entidade2 import LeitosResponse , LocationResponse , GestaoResponse
from sqlalchemy.orm import Session

entidade2 = APIRouter(prefix = "/entidade2" , tags=['entidade2'])


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
    cod = session.query(Location).filter(Location.cod_uf_municipio == cod_uf).first()
    if not user:
        raise HTTPException(status_code = 400 , detail = "Usuario não autenticado")
    session.commit()
    session.refresh(cod)
    return cod
    
@entidade2.put("/entidade2/{id}", response_model = LocationResponse)
async def update(id: str , data: LocationCreate , session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    cod = session.query(Location).filter(Location.id == id).first()
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    cod.cod_uf_municipio = data.cod_uf_municipio
    cod.regiao_saude = data.regiao_saude
    cod.microregiao = data.microregiao
    session.commit()
    session.refresh(cod)
    return cod

@entidade2.delete("/delete_location/{id}")
async def delete(id: str , session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    cod = session.query(Location).filter(Location.id == id).first()
    if not cod:
        raise HTTPException(status_code = 400 , detail = "Registro não encontrado")
    
    session.delete(cod)
    session.commit()
    return cod

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
    update = session.query(Gestao).filter(Gestao.id == id).first()
    if not update:
        raise HTTPException(status_code = 400 , detail = f"Registro com id={id} não encontrado")
    update.tipo_gestao = data.tipo_gestao
    update.esfera_admin = data.esfera_admin
    update.retencao = data.retencao

    session.commit()
    return update

@entidade2.delete("/Gestao_delete/{id}")
async def delete_gse(id: str , session: Session = Depends(pegar_sessao) , user: Session = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autenticator")
    GseDelete = session.query(Gestao).filter(Gestao.id == id).first()
    if not GseDelete:
        raise HTTPException(status_code = 400 , detail = "Cadastro not encontrado")
    session.delete(GseDelete)
    session.commit()
    return GseDelete

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

@entidade2.put("/update_leitos", response_model = LocationResponse)
async def update_get_leitos(id: str , data: LeitosCreate , session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "user not autheticator")
    leitos = session.query(Leitos).filter(Leitos.id == id).first()
    leitos.leitos_tipo_1 = data.leitos_tipo_1
    leitos.leitos_tipo_2 = data.leitos_tipo_2
    leitos.leitos_tipo_3 = data.leitos_tipo_3
    leitos.total_leitos = data.total_leitos
    session.commit()
    session.refresh(leitos)
    return leitos

@entidade2.delete("/delete_leitos/{id}")
async def delete_leitos(id: str , session: Session = Depends(pegar_sessao) , user = Depends(verificar_token)):
    if not user:
        raise HTTPException(status_code = 400 , detail = "User not autheticator")
    leitos = session.query(Leitos).filter(Leitos.id == id).first()
    if not leitos:
        raise HTTPException(status_code = 400 , detail = "Cadastro não encontrado !")
    session.delete(leitos)
    session.commit()
    return leitos