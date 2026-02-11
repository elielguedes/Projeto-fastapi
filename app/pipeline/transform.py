import pandas as pd

def transform_cnes(df: pd.DataFrame) -> dict:

    df.columns = df.columns.str.strip().str.upper()

    df = df.dropna(axis = 1 , how = "all")

    df = df[df["CNES"].notna()]

    colunas_unidade = [
        "CNES", "TP_UNID", "NATUREZA",
        "ESFERA_A" , "VINC_SUS",
        "NAT_JUR", "CODUFMUN"
    ]

    colunas_unidade = [c for c in colunas_unidade if c in df.columns]
    df_unidade = df[colunas_unidade]

    colunas_location = ["CODUFMUN", "REGSAUDE", "MICR_REG"]
    colunas_location = [c for c in colunas_location if c in df.columns]
    df_location = df[colunas_location]

    colunas_gestao = ["TPGESTAO", "ESFERA_A", "RETENCAO", "VINC_SUS"]
    colunas_gestao = [c for c in colunas_gestao if c in df.columns]
    df_gestao = df[colunas_gestao]

    colunas_leitos = ["QTLEITP1" , "QTLEITP2" , "QTLEITP3", "LEITHOSP"]
    colunas_leitos = [c for c in colunas_leitos if c in df.columns]
    df_leitos = df[colunas_leitos].fillna(0)
    df_leitos[colunas_leitos] = df_leitos[colunas_leitos].astype(int)

    return {
        "unidade": df_unidade,
        "location": df_location,
        "gestão": df_gestao,
        "leitos": df_leitos
    }



