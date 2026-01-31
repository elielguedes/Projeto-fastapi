from fastapi import FastAPI 
from app.routes.auth import auth
from .routes.entidade1 import entidade1
from .routes.entidade2 import entidade2

app = FastAPI()

app.include_router(auth)
app.include_router(entidade1)
app.include_router(entidade2)
@app.get("/")
def root():
    return {"status": "ok"}