import os
import csv
from sqlalchemy import text
from app.database import engine
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "csv" / "cnes.csv"

print(f"lendo arquivo: {CSV_PATH}")

with engine.begin() as conn:
    with open(CSV_PATH , newline = "" , encoding = "latin-1") as csvfile:
        reader = csv.DictReader(csvfile)

        print("colunas reais: ", reader.fieldnames)

        for row in reader:
            unidade = conn.execute(
                text("SELECT id FROM unidade_saude WHERE cnes = :cnes"),
                {"cnes": row["CNES"]}
            ).fetchone()

            if not unidade:
                print(f"Unidade não encontrada para CNES {row['CNES']}")
                continue

            conn.execute(
                text("""INSERT INTO location(
                     cod_uf_municipio,
                     regiao_saude,
                     microregiao,
                     unidade_id
                     )VALUES (
                     :cod_uf,
                     :regiao,
                     :micro,
                     :unidade_id
                     )"""),
                     {
                         "cod_uf": row["CODUFMUN"],
                         "regiao": row.get("REGIAO_SAUDE"),
                         "micro": row.get("MICROREGIAO"),
                         "unidade_id": unidade.id
                     }
            )
print("LOCATION importado corretamente")
