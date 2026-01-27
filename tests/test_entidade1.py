import os 
os.environ["DATABASE_URL_TEST"] = "sqlite:///./test.db"

import pytest
from fastapi.testclient import TestClient
from app.database import  Base 
from app.main import app
from tests.databasetests import engine_test , SessionTests
from app.core.config import verificar_token
from sqlalchemy import text

def fake_verificar_token():
    return {"id": 1 ,"email": "teste@gmail.com"}

app.dependency_overrides[verificar_token] = fake_verificar_token

client = TestClient(app)

@pytest.fixture(scope = "session" , autouse = True)
def setup():
    Base.metadata.create_all(bind = engine_test)
    yield
    Base.metadata.drop_all(bind = engine_test)

@pytest.fixture(scope = "function" , autouse = True)
def clear_tables():
    with engine_test.begin() as conn:
        conn.execute(text("DELETE FROM unidade_saude"))
# ===== Unidade =====
def test_unidade_create():
    res = client.post("/unidade-saude/create" , json = {
        "cnes": "1234567",
        "nome": "Unidade teste"
    })

    assert res.status_code in (200 , 400)

def test_unidade_update():
    res = client.post("/unidade-saude/create", json = {
        "cnes": "1234567",
        "nome": "Unidade teste"
    })

    res = client.put("/unidade-saude/update/1234567", json = {
        "nome": "Unidade alterada"
    })
    assert res.status_code == 200

def test_update_nao_existe():
    res = client.put("/unidade-saude/update/1234567", json = {
        "nome": "Unidade teste"
    })

    assert res.status_code == 404

def test_unidade_lista():
    res = client.get("/unidade-saude/lista")
    assert res.status_code == 200
    data = res.json()
    print (data)

def test_unidade_delete():
    client.post("/unidade-saude/create", json = {
        "cnes": "1234567",
        "nome": "Unidade teste"
    })
    res = client.delete("/unidade-saude/delete/1234567")

    assert res.status_code in (200 , 400)