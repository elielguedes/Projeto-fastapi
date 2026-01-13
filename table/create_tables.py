from app.database import engine, Base
from app.models import UnidadeSaude, Location, Gestao, Leitos 
from app.models.user import User

Base.metadata.create_all(bind=engine)
print("✅ Tabelas criadas")
