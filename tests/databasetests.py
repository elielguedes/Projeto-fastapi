from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool # ==== Gerenciamento de conexao ====
from app.database import Base

DATABASE_URL_TEST = "sqlite:///./test.db"

engine_test = create_engine(DATABASE_URL_TEST , connect_args = {"check_same_thread": False} , poolclass=StaticPool)

SessionTests = sessionmaker(autocommit = False , autoflush = False , bind = engine_test)


