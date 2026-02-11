from ..pipeline.extract import extract_cnes
from ..pipeline.transform import transform_cnes
from ..pipeline.load import load_to_db

def run_pipeline():
    print("\n === Iniciando pipeline CNES === \n")

    df_raw = extract_cnes()
    print(f"Extraído:  {df_raw.shape}")

    dfs_trusted = transform_cnes(df_raw)
    print("Transformação concluída")

    load_to_db(dfs_trusted)
    print("Dados Carregados no banco")

    print("Pipeline finalizado no banco")

if __name__ == "__main__":
    run_pipeline()