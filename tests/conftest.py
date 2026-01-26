from app.database import pegar_sessao
from app.main import app
from tests.databasetests import SessionTests

def override_pegar_sessao():
    db = SessionTests()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[pegar_sessao] = override_pegar_sessao