from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import os

DATABASE_URL = os.getenv("DATABASE" , "sqlite:///./app.db")

engine = create_engine(DATABASE_URL , connect_args={"check_same_thread": False})

Base = declarative_base()