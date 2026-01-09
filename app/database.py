from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base , sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE" , "sqlite:///./app.db")

if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL , connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)



Base = declarative_base()

SessionLocal = sessionmaker(autocommit = False , autoflush = False , bind = engine)

def pegar_sessao():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
