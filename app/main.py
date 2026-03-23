from fastapi import FastAPI , Request , HTTPException
from app.routes.auth import auth
from .routes.entidade1 import entidade1
from .routes.entidade2 import entidade2
from .core.logs import setup_loguin
from .routes.pipeline import router
import logging

setup_loguin()

logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(auth)
app.include_router(entidade1)
app.include_router(entidade2)
app.include_router(router)

logger = logging.getLogger(__name__)
logger.info("API Iniciada")
logger.error("Deu ruim aqui")

@app.get("/")
def root():
    return {"status": "ok"}

