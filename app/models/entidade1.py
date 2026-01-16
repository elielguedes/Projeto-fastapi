from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class UnidadeSaude(Base):
    __tablename__ = "unidade_saude"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cnes = Column(String(7), unique=True, index=True , nullable = False)
    nome = Column(String(255))
    location = relationship("Location", back_populates="unidade", uselist=False)
    gestao = relationship("Gestao", back_populates="unidade", uselist=False)
    leitos = relationship("Leitos", back_populates="unidade", uselist=False)
