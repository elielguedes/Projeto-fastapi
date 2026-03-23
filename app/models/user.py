from sqlalchemy import Column, String , Boolean
from app.database import Base
from sqlalchemy.orm import Mapped , mapped_column
import uuid

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True , default = lambda: str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String, nullable=False)
    perfil: Mapped[bool] = mapped_column(Boolean, default=False)
