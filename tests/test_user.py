import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base
from tests.databasetests import engine_test , SessionTests


os.environ["DATABASE_URL_TEST"] = "sqlite:///./test.db"

client = TestClient(app)

@pytest.fixture(scope = 'session' , autouse = True)
def setup():
    Base.metadata.create_all(bind = engine_test)
    yield
    Base.metadata.drop_all(bind = engine_test)

def test_registre_and_loguin():
    response = client.post("/auth/create_user" , json = {
        "name": "name",
        "email": "email@email.com",
        "senha": "senha",
        "perfil": True
    })

    assert response.status_code in (200 , 400)

def test_user_loguin():
    res = client.post("/auth/Loguin", json = {
        "email": "email@email.com",
        "senha": "senha"
    })
    assert res.status_code in (200 , 400)

def test_user_form():
    res = client.post("/auth/loguin-form", data = {
        "username": "email@email.com",
        "password": "senha"
    })
    assert res.status_code == 200
    body = res.json()
    assert "access_token" in body
    assert body["token_type"] == "bearer"