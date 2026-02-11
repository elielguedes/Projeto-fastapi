import pandas as pd

CSV_PATH = "csv/cnes.csv"

def extract_cnes() -> pd.DataFrame:
    df = pd.read_csv(CSV_PATH , sep="," , encoding = "latin1", low_memory = False)
    return df 