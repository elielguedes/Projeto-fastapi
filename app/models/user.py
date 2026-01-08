from sqlalchemy import create_engine , Column, String , Integer , Boolean 
from sqlalchemy.orm import declarative_base
from uuid import UUID
from pydantic import EmailStr
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True , autoincrement = True)
    name = Column(String)
    email = Column(String)
    perfil = Column(Boolean)

