from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class UnidadeSaude(Base):
    __tablename__ = "unidade_saude"

    id = Column(String(36), primary_key=True, default = lambda: str(uuid.uuid4()))
    cnes = Column(String(7), unique=True, index=True , nullable = False)
    nome = Column(String(255))
    location = relationship("Location", back_populates="unidade", uselist=False)
    gestao = relationship("Gestao", back_populates="unidade", uselist=False)
    leitos = relationship("Leitos", back_populates="unidade", uselist=False)
