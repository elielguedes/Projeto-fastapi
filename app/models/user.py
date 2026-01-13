from sqlalchemy import Column, Integer, String , Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    perfil = Column(Boolean, default=False)
