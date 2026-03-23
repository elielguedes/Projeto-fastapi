from sqlalchemy import String 
from sqlalchemy.orm import Mapped , mapped_column , relationship
from app.database import Base
import uuid

class UnidadeSaude(Base):
    __tablename__ = "unidade_saude"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default = lambda: str(uuid.uuid4()))
    cnes: Mapped[str] = mapped_column(String(7), unique=True, index=True , nullable = False)
    nome: Mapped[str] = mapped_column(String(255))
    location = relationship("Location", back_populates="unidade", uselist=False , cascade="all , delete-orphan")
    gestao = relationship("Gestao", back_populates="unidade", uselist=False , cascade="all ,delete-orphan")
    leitos = relationship("Leitos", back_populates="unidade", uselist=False , cascade="all , delete-orphan")