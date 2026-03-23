from sqlalchemy import String , Integer , ForeignKey
from sqlalchemy.orm import relationship , Mapped , mapped_column 
from app.database import Base
import uuid

class Location(Base):
    __tablename__ = "location"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default = lambda: str(uuid.uuid4()))

    cod_uf_municipio: Mapped[int] = mapped_column(Integer, nullable=False)
    regiao_saude: Mapped[str] = mapped_column(String(100))
    microregiao: Mapped[str] = mapped_column(String(100))

    unidade_id: Mapped[str] = mapped_column(String(36) , ForeignKey("unidade_saude.id", ondelete = "CASCADE"), nullable = False)
    unidade = relationship("UnidadeSaude", back_populates="location")

class Gestao(Base):
    __tablename__ = "gestao"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default = lambda: str(uuid.uuid4()))

    tipo_gestao: Mapped[str] = mapped_column(String(10))
    esfera_admin: Mapped[str] = mapped_column(String(10))
    retencao: Mapped[str] = mapped_column(String(10))
    unidade_id: Mapped[str] = mapped_column(String(36) ,ForeignKey("unidade_saude.id", ondelete = "CASCADE") , nullable = False)
    unidade = relationship("UnidadeSaude", back_populates="gestao")

class Leitos(Base):
    __tablename__ = "leitos"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default = lambda: str(uuid.uuid4()))

    leitos_tipo_1: Mapped[int] = mapped_column(Integer, default=0)
    leitos_tipo_2: Mapped[int] = mapped_column(Integer, default=0)
    leitos_tipo_3: Mapped[int] = mapped_column(Integer, default=0)
    total_leitos: Mapped[int] = mapped_column(Integer, default=0)

    unidade_id: Mapped[str] = mapped_column(String(36) , ForeignKey("unidade_saude.id" , ondelete = "CASCADE"), nullable = False)
    unidade = relationship("UnidadeSaude", back_populates="leitos")