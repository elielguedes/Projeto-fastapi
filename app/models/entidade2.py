from sqlalchemy import create_engine , Column , String , Integer , Boolean , ForeignKey
from sqlalchemy.orm import declarative_base , relationship
from app.database import Base

class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True, autoincrement=True)

    cod_uf_municipio = Column(Integer, nullable=False)
    regiao_saude = Column(String(100))
    microregiao = Column(String(100))

    unidade_id = Column(Integer , ForeignKey("unidade_saude.id", ondelete = "CASCADE"), nullable = False)
    unidade = relationship("UnidadeSaude", back_populates="location")

class Gestao(Base):
    __tablename__ = "gestao"

    id = Column(Integer, primary_key=True, autoincrement=True)

    tipo_gestao = Column(String(10))
    esfera_admin = Column(String(10))
    retencao = Column(String(10))
    unidade_id = Column(Integer ,ForeignKey("unidade_saude.id", ondelete = "CASCADE") , nullable = False)
    unidade = relationship("UnidadeSaude", back_populates="gestao")

class Leitos(Base):
    __tablename__ = "leitos"

    id = Column(Integer, primary_key=True, autoincrement=True)

    leitos_tipo_1 = Column(Integer, default=0)
    leitos_tipo_2 = Column(Integer, default=0)
    leitos_tipo_3 = Column(Integer, default=0)
    total_leitos = Column(Integer, default=0)

    unidade_id = Column(Integer , ForeignKey("unidade_saude.id" , ondelete = "CASCADE"), nullable = False)
    unidade = relationship("UnidadeSaude", back_populates="leitos")