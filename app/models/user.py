from sqlalchemy import Column, Integer, String , Boolean
from app.database import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True , default = lambda: str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    perfil = Column(Boolean, default=False)
