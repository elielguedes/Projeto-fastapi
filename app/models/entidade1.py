from sqlalchemy import create_engine , Column , String , Integer , Boolean
from sqlalchemy.orm import declarative_base
from uuid import UUID
from app.database import Base

class unidade_de_saude(Base):
    __tablename__ = "UNIDADE_SAUDE"

    id = Column(Integer, primary_key = True , autoincrement = True)
    Cnes = Column(Integer)
    tipo_unidade = Column(String)
    veiculos_sus = Column(String)
