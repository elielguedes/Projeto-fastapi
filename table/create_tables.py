from app.database import engine, Base
from app.models.entidade1 import UnidadeSaude
from app.models.entidade2 import Location, Gestao, Leitos 
from app.models.user import User

Base.metadata.create_all(bind=engine)
print("✅ Tabelas criadas")
