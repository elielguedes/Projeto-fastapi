from ..pipeline.extract import extract_cnes
from ..pipeline.transform import transform_cnes
from ..pipeline.load import load_to_db
from ..pipeline.metrics import PipelineMetrics
import logging

logger = logging.getLogger(__name__)


def run_pipeline():
    metrics = PipelineMetrics()
    print("\n === Iniciando pipeline CNES === \n")
    metrics.start()

    try:
        df_raw = extract_cnes()
        metrics.row_extracted = len(df_raw)
        print(f"Extraído: {df_raw.shape}")
        
        if df_raw.empty:
            raise ValueError("Arquivo Cnes Veio Vazio")
        dfs_trusted = transform_cnes(df_raw)
        print("Transformação concluída ")
        load_to_db(dfs_trusted)
        metrics.row_loaded = len(df_raw)
        print("Dados Carregado no Banco")

        metrics.finish(success = True)
        print("Pipeline Finalizado no banco")
    except Exception as e:
        metrics.finish(success = False)
        logger.critical("Pipeline Cnes falhou", exc_info = True)
        raise
if __name__ == "__main__":
    run_pipeline()