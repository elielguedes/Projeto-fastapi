from fastapi import HTTPException
from ..models.entidade1 import UnidadeSaude
from sqlalchemy.orm import Session
from ..schemas.entidade1 import UnidadeCreator ,  UnidadeUpdate
from ..repositoryes.entidade1 import SaudeRepository

class SaudeService:
    def __init__(self , repository: SaudeRepository):
        self.repository = repository
    

    def create_unidade(self, unidade: UnidadeCreator):
        db_unidade = UnidadeSaude(cnes = unidade.cnes ,nome = unidade.nome)
        if not unidade.cnes:
            raise HTTPException(status_code = 400 , detail = "CNES Invalido")
        return self.repository.create(db_unidade)


    def update_unidade_service(self , cnes: str , dados: UnidadeUpdate):
        unidade = self.repository.get_by_cnes(cnes)
        if not unidade:
            raise HTTPException(status_code = 404 , detail = f"Unidade {cnes} não encontrada")
        unidade.nome = dados.nome
        return self.repository.update(unidade)

    def delete_unidade_service(self , cnes: str , db: Session):
        unidade = self.repository.del_by_cnes(cnes)
        if not unidade:
            raise HTTPException(status_code = 400 , detail = "CNES não encontrado")
        self.repository.delete(unidade)
        return {"mensagem": f"Unidade {cnes} removida com sucesso"}