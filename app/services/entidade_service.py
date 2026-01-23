from fastapi import HTTPException
from sqlalchemy.orm import Session 
from ..models.entidade2 import Location , Gestao , Leitos
from ..schemas.entidade2 import LocationCreate , GestaoCreate , LeitosCreate

def get_service_uf(db: Session ,cod_uf: int):
    cod = db.query(Location).filter(Location.cod_uf_municipio == cod_uf).first()
    if not cod:
        raise HTTPException(status_code = 400 , detail = "Código UF não encontrado")
    db.commit()
    db.refresh(cod)
    return cod


def update_id_lct(id: str , db: Session , data: LocationCreate):
    cod = db.query(Location).filter(Location.id == id).first()
    if not cod:
        raise HTTPException(status_code = 400 , detail = "Cadastro não encontrado")
    
    cod.cod_uf_municipio = int(data.cod_uf_municipio)
    cod.regiao_saude = data.regiao_saude
    cod.microregiao = data.microregiao
    db.commit()
    db.refresh(cod)
    return cod

def delete_service_lct(id: str , db: Session):
    cod = db.query(Location).filter(Location.id == id).first()
    if not cod:
        raise HTTPException(status_code = 400 , detail = "Registro não encontrado")
    
    db.delete(cod)
    db.commit()
    return cod


def update_service_gse(id: str ,data: GestaoCreate , db: Session):
    update = db.query(Gestao).filter(Gestao.id == id).first()
    if not update:
        raise HTTPException(status_code = 400 , detail = f"Registro com id={id} não encontrado")
    update.tipo_gestao = data.tipo_gestao
    update.esfera_admin = data.esfera_admin
    update.retencao = data.retencao

    db.commit()
    return update

def delete_service_gse(id: str , db: Session):
    GseDelete = db.query(Gestao).filter(Gestao.id == id).first()
    if not GseDelete:
        raise HTTPException(status_code = 400 , detail = "Cadastro not encontrado")
    
    db.delete(GseDelete)
    db.commit()
    return GseDelete

def put_service_leitos(id: str ,data: LeitosCreate , db: Session):
    leitos = db.query(Leitos).filter(Leitos.id == id).first()
    if not leitos:
        raise HTTPException(status_code = 400 , detail = "Cadastros não encontrados")
    
    if data.leitos_tipo_1 is not None:
        leitos.leitos_tipo_1 = data.leitos_tipo_1
    
    if data.leitos_tipo_1 is not None:
        leitos.leitos_tipo_2 = data.leitos_tipo_2
    
    if data.leitos_tipo_3 is not None:
        leitos.leitos_tipo_3 = data.leitos_tipo_3
    leitos.total_leitos = (leitos.leitos_tipo_1 or 0) + (leitos.leitos_tipo_2 or 0) + (leitos.leitos_tipo_3 or 0)
    db.commit()
    db.refresh(leitos)
    return leitos

def delete_service_leitos(id: str , db: Session):
    leitos = db.query(Leitos).filter(Leitos.id == id).first()
    if not leitos:
        raise HTTPException(status_code = 400 , detail = "Cadastro não encontrado !")
    db.delete(leitos)
    db.commit()
    return leitos