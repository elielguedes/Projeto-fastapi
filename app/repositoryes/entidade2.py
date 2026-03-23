from sqlalchemy.orm import Session
from ..models.entidade2 import Location , Gestao , Leitos

class EntidadeRepositoryes:
    def __init__(self, db: Session):
        self.db = db
    
    # Location
    def get_by_coduf(self , cod_uf: int):
        return self.db.query(Location).filter(Location.cod_uf_municipio == cod_uf).all()
    
    def get_up_id(self , id: str):
        return self.db.query(Location).filter(Location.id == id).first()
    
    def update(self , id: str):
        self.db.commit()
        self.db.refresh(id)
        return id
    
    def get_delete_loc(self , id: str):
        return self.db.query(Location).filter(Location.id == id).first()
    
    def del_loc(self, id: str):
        self.db.delete(id)
        self.db.commit()
        return id
    
    # Getao
    def get_by_id(self , id: str):
        return self.db.query(Gestao).filter(Gestao.id == id).first()
    
    def update_gse(self , id: str):
        self.db.commit()
        self.db.refresh(id)
        return id
    
    def get_by_gestao(self):
        return self.db.query(Gestao).all()
    
    def get_by_tipo(self ,tipo_gse: str):
        return self.db.query(Gestao).filter(Gestao.tipo_gestao == tipo_gse).first()

    def delete_gestao(self , id: str):
        self.db.delete(id)
        self.db.commit()
        return id
    
    # Leitos
    def get_by_leito(self , id: str):
        return self.db.query(Leitos).filter(Leitos.id == id).first()
    
    def put_leitos(self , id: str):
        self.db.commit()
        self.db.refresh(id)
        return id
    
    def del_leitos(self , id: str):
        self.db.delete(id)
        self.db.commit()
        return id
    
    def get(self):
        return self.db.query(Leitos).all()