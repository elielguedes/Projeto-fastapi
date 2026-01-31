from fastapi import FastAPI , Request , HTTPException
from app.routes.auth import auth
from .routes.entidade1 import entidade1
from .routes.entidade2 import entidade2
from .core.logs import setup_loguin
import logging

setup_loguin()

logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(auth)
app.include_router(entidade1)
app.include_router(entidade2)

logger = logging.getLogger(__name__)
logger.info("API Iniciada")
logger.error("Deu ruim aqui")

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/tests")
async def tests():
    try:
        logger.info("Rota '/tests' acessada")
        res = 10/2
        logger.info(f"Resultado do tests: ", {res})
        return {"res": res}
    except Exception as e:
        logger.error(f"Deu ruim na rota /tests: {e}")
        raise HTTPException(status_code = 500 , detail = "Erro no servidor interno")
        