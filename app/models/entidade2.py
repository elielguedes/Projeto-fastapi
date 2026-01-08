from sqlalchemy import create_engine , Column , String , Integer , Boolean , ForeignKey
from sqlalchemy.orm import declarative_base
from uuid import UUID
from enum import Enum
from pydantic import field_validator
from app.database import Base

class Location(Base):
    __tablename__ = "Lacalization"

    id = Column(Integer, primary_key = True ,  autoincrement = True)
    cod_uf_municipio = Column(Integer)
    regiao_saude = Column(String)
    microregiao = Column(String)

    unidade_id = Column(Integer, ForeignKey("UNIDADE_SAUDE.id"))

class Gestao(Base):
    __tablename__ = "Gestao"

    id = Column(Integer, primary_key = True , autoincrement = True)
    tipo_gestao = Column("tipo_gse", String)
    esfera_admin = Column("esfer_adm", Boolean)
    retencao = Column("retencao", String)
    
    unidade_id = Column(Integer, ForeignKey("UNIDADE_SAUDE.id"))

class leitos(Base):
    __tablename__ = "Leitos"

    id = Column(Integer, primary_key = True , autoincrement = True)
    leitos_tipo_1 = Column(Integer)
    leitos_tipo_2 = Column(Integer)
    leito_tipo_3 = Column(Integer)
    total_leitos = Column(Integer)

    unidade_id = Column(Integer , ForeignKey("UNIDADE_SAUDE.id"))