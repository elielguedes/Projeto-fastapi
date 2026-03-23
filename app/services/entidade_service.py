from fastapi import HTTPException
from sqlalchemy.orm import Session 
from ..models.entidade2 import Location , Gestao , Leitos
from ..schemas.entidade2 import LocationCreate , GestaoCreate , LeitosCreate
from ..models.entidade1 import UnidadeSaude
from ..repositoryes.entidade2 import EntidadeRepositoryes
# ==== Location ====
class EntidadeService:
    def __init__(self , repository: EntidadeRepositoryes):
        self.repository = repository
    
    def get_service_uf(self, cod_uf: int):
        codigouf = self.repository.get_by_coduf(cod_uf)
        if not codigouf:
            raise HTTPException(status_code = 400 , detail = "Código UF não encontrado")
        return codigouf

    def update_id_lct(self, data: LocationCreate , id: str):
        cod = self.repository.get_up_id(id)
        if not cod:
            raise HTTPException(status_code = 400 , detail = "Cadastro não encontrado")
    
        cod.cod_uf_municipio = int(data.cod_uf_municipio)
        cod.regiao_saude = str(data.regiao_saude)
        cod.microregiao = str(data.microregiao)
        return self.repository.update(cod)

    def delete_service_lct(self ,id: str , db: Session):
        codi = self.repository.get_delete_loc(id)
        if not codi:
            raise HTTPException(status_code = 404 , detail = "Registro não encontrado")
        
        return self.repository.del_loc(codi)

    # ==== Gestao ====
    def update_service_gse(self ,data: GestaoCreate , id: str):
        update = self.repository.get_by_id(id)
        if not update:
            raise HTTPException(status_code = 400 , detail = f"Registro com id={id} não encontrado")
        update.tipo_gestao = data.tipo_gestao
        update.esfera_admin = data.esfera_admin
        update.retencao = data.retencao
        return self.repository.update_gse(update)

    def delete_service_gse(self ,id: str):
        GseDelete = self.repository.get_by_id(id)
        if not GseDelete:
            raise HTTPException(status_code = 404 , detail = "Cadastro not encontrado")
        return self.repository.delete_gestao(GseDelete)

# ==== Leitos ====
    def put_service_leitos(self ,id: str ,data: LeitosCreate):
        leitos = self.repository.get_by_leito(id)
        if not leitos:
            raise HTTPException(status_code = 400 , detail = "Cadastros não encontrados")
    
        if data.leitos_tipo_1 is not None:
            leitos.leitos_tipo_1 = data.leitos_tipo_1
    
        if data.leitos_tipo_1 is not None:
            leitos.leitos_tipo_2 = data.leitos_tipo_2
    
        if data.leitos_tipo_3 is not None:
            leitos.leitos_tipo_3 = data.leitos_tipo_3
        leitos.total_leitos = (leitos.leitos_tipo_1 or 0) + (leitos.leitos_tipo_2 or 0) + (leitos.leitos_tipo_3 or 0)
        return self.repository.put_leitos(leitos)

    def delete_service_leitos(self , id: str):
        leitos = self.repository.get_by_leito(id)
        if not leitos:
            raise HTTPException(status_code = 400 , detail = "Cadastro não encontrado !")
        return self.repository.del_leitos(leitos)