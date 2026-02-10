import pandas as pd

# Carrega o CSV
df = pd.read_csv(
    "csv/cnes.csv",
    sep=",",
    encoding="latin1",
    low_memory=False
)

# Normaliza os nomes das colunas (remove espaços e coloca em maiúsculo)
df.columns = df.columns.str.strip().str.upper()

print(df.shape)
print(df.columns.tolist())

# Remove colunas totalmente vazias
df = df.dropna(axis=1, how="all")

# Remove linhas sem CNES (registro inválido)
df = df[df["CNES"].notna()]

# Seleções de colunas
colunas_unidade = ["CNES", "TP_UNID", "NATUREZA", "ESFERA_A", "VINC_SUS", "NAT_JUR", "CODUFMUN"]
colunas_unidade = [c for c in colunas_unidade if c in df.columns]
df_unidade = df[colunas_unidade]

colunas_location = ["CODUFMUN", "REGSAUDE", "MICR_REG"]
colunas_location = [c for c in colunas_location if c in df.columns]
df_location = df[colunas_location]

colunas_gestao = ["TPGESTAO", "ESFERA_A", "RETENCAO", "VINC_SUS"]
colunas_gestao = [c for c in colunas_gestao if c in df.columns]
df_gestao = df[colunas_gestao]

colunas_leitos = ["QTLEITP1", "QTLEITP2", "QTLEITP3", "LEITHOSP"]
colunas_leitos = [c for c in colunas_leitos if c in df.columns]
df_leitos = df[colunas_leitos].fillna(0)

# Converte para inteiro
df_leitos[colunas_leitos] = df_leitos[colunas_leitos].astype(int)

# Exporta cada DataFrame para um CSV separado
df_unidade.to_csv("unidade_unidade.csv", index=False, encoding="utf-8")
df_location.to_csv("unidade_location.csv", index=False, encoding="utf-8")
df_gestao.to_csv("unidade_gestao.csv", index=False, encoding="utf-8")
df_leitos.to_csv("unidade_leitos.csv", index=False, encoding="utf-8")

print("csvs organizados!")
