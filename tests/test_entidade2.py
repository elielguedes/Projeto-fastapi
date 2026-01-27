import os
os.environ["DATABASE_URL_TEST"] = "sqlite:///./test.db"

from fastapi.testclient import TestClient
import pytest
from app.database import Base
from app.main import app
from tests.databasetests import engine_test
from app.core.config import verificar_token
from sqlalchemy import text
from app.models.entidade2 import Location
from app.database import SessionLocal

def token_fake():
    return {"id": "test-user" , "email": "teste@gmail.com"}

app.dependency_overrides[verificar_token] = token_fake

client = TestClient(app)

@pytest.fixture(scope = "session" , autouse = True)
def setup():
    # ===== Tabelas =====
    Base.metadata.create_all(bind = engine_test)
    yield
    Base.metadata.drop_all(bind = engine_test)

# ===== Location ======
def tests_get_location():
    res = client.get("/entidade2/listar-location")
    assert res.status_code == 200

def get_location_uf():
    res = client.get("/entidade2/Location" , params = {"cod_uf": 230440})

    assert res.status_code == 200

def put_location():
    res = client.put("/entidade2/entidade2/b3a90260-d11b-43d0-9af4-d0e2363001d3", json = {
        "cod_uf_municipio": "230441",
        "regiao_saude": "1",
        "microregiao": "1"
    })

    assert res.status_code in (200 , 400)


def test_locate_delete():
    res = client.delete("/entidade2/delete_location/b3a90260-d11b-43d0-9af4-d0e2363001d3")

    assert res.status_code == 404
    data = res.json()
    assert data["detail"] == "Registro não encontrado"
# ===== Gestao =====
def test_get_gestao():
    res = client.get("/entidade2/gestao")
    assert res.status_code == 200

def tests_get_id():
    res = client.get("/entidade2/gestao/de4c13b1-bd46-4188-8e7c-4e9689032292", params = {"id": "de4c13b1-bd46-4188-8e7c-4e9689032292"})

def tests_get_tipo():
    res = client.get("/entidade2/gestao", params = {
        "tipo_gse": "M"
    })

def tests_put_gse():
    res = client.put("/entidade2/gestao_update?id=de4c13b1-bd46-4188-8e7c-4e9689032292", json = {
        "tipo_gestao": "M",
        "esfera_admin": "",
        "retencao": ""
    })

    assert res.status_code in (200 , 400)

def tests_delete_gestao():
    res = client.delete("/entidade2/gestao_delete/de4c13b1-bd46-4188-8e7c-4e9689032292" , params = {"id": "de4c13b1-bd46-4188-8e7c-4e9689032292"})

    assert res.status_code in (200 , 404)
# ===== Leitos =====
def tests_get_leitos():
    res = client.get("/entidade2/leitos")

    assert res.status_code == 200

def tests_get_leitos_id():
    res = client.get("/entidade2/leitos/6627b05b-ebe3-411b-b5df-8f1840daa356" , params = {
        "id": "6627b05b-ebe3-411b-b5df-8f1840daa356",
        "leitos_tipo_1": "0",
        "leitos_tipo_2": "0",
        "leitos_tipo_3": "0",
        "total_leitos": "0"

    })

    assert res.status_code in (200 , 400)

def tests_put_leitos():
    res = client.put("/entidade2/update_leitos/6627b05b-ebe3-411b-b5df-8f1840daa356" , json = {
        "leitos_tipo_1": "1",
        "leitos_tipo_2": "1",
        "leitos_tipo_3": "1",
        "total_leitos": "3"
    })

    assert res.status_code in (200 , 400)

def tests_detele_leitos():
    res = client.delete("/entidade2/delete_leitos/6627b05b-ebe3-411b-b5df-8f1840daa356" , params = {
        "id": "6627b05b-ebe3-411b-b5df-8f1840daa356"
    })

    assert res.status_code in (200 , 400)