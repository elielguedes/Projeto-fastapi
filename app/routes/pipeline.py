from fastapi import APIRouter , Depends
from ..pipeline.pipeline import run_pipeline
from ..core.config import verificar_adm

router = APIRouter()

@router.post("/pipeline/run" , tags=['pipeline'] , summary = "Execultar piperline")
def executar(user = Depends(verificar_adm)):
    run_pipeline()
    return {"mensagem": "Pipeline executado com sucesso"}