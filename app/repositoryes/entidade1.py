from sqlalchemy.orm import Session
from ..models.entidade1 import UnidadeSaude 


class SaudeRepository:
    def __init__(self , db: Session):
        self.db = db
    
    def create(self , unidade: UnidadeSaude):
        self.db.add(unidade)
        self.db.commit()
        self.db.refresh(unidade)
        return unidade
    
    def get_by_cnes(self , cnes: str):
        return self.db.query(UnidadeSaude).filter(UnidadeSaude.cnes == cnes).first()

    def update(self , unidade: UnidadeSaude):
        self.db.commit()
        self.db.refresh(unidade)
        return unidade
    
    def del_by_cnes(self , cnes: str):
        return self.db.query(UnidadeSaude).filter(UnidadeSaude.cnes == cnes).first()
    
    def delete(self , cnes: str):
        self.db.delete(cnes)
        self.db.commit()
        return cnes