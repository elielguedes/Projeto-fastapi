import pandas as pd

df = pd.read_csv(
    "csv/cnes.csv",
    sep=",",
    encoding = "latin1",
    low_memory = False
)

print (df.shape)
print(df.columns.tolist())

#remove colunas totalmente vazias
df = df.dropna(axis=1 , how="all")

#remove linhas sem cnes (registro inválido)
df = df[df["CNES"].notna()]
colunas_unidade = [
    "CNES",
    "TP_UNID",
    "NATUREZA",
    "ESFERA_A",
    "VINC_SUS",
    "NAT_JUR",
    "CODUFMUN"
]
df_unidade = df[colunas_unidade]

colunas_location = df[[
    "CODUFMUN",
    "REGSAUDE",
    "MICR_RG"
]]
df_location = df[colunas_location]

colunas_gestao = df[[
    "TPGESTAO",
    "ESFERA_A",
    "RETENCAO",
    "VINC_SUS"
]]

df_gestao = df[colunas_gestao]

colunas_leitos = df[[
    "QTLEITP1",
    "QTLEITP2",
    "QTLEITP3",
    "LEITHOSP"
]]
df_leitos = df[colunas_leitos]

df_leitos = df[colunas_leitos].fillna(0)
df.columns = df.columns.str.strip()

df_leitos[colunas_leitos] = df_leitos[colunas_leitos].astype(int)

df_unidade.to_csv("unidade_limpo.csv" , index = False , encoding = "utf-8")
df_location.to_csv("unidade_limpo.csv" , index = False , encoding = "utf-8")
df_gestao.to_csv("unidade_limpo.csv" , index = False , encoding = "utf-8")
df_leitos.to_csv("unidade_limpo.csv" , index = False , encoding = "utf-8")

print ("csvs organizados !")