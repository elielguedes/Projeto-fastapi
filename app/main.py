from fastapi import FastAPI 
from app.routes.auth import auth
from .routes.entidade1 import entidade1

app = FastAPI()

app.include_router(auth)
app.include_router(entidade1)