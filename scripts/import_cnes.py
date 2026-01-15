import os
import csv
from sqlalchemy import text
from app.database import engine

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "csv", "CNES.csv")

print("📂 Lendo arquivo:", CSV_PATH)

with open(CSV_PATH, encoding="latin-1", newline="") as f:
    reader = csv.DictReader(
        f,
        delimiter=",",        # 👈 CORRETO
        quotechar='"'         # 👈 IMPORTANTE
    )

    print("📌 Colunas reais:", reader.fieldnames[:5])  # debug rápido

    with engine.begin() as conn:
        for row in reader:
            conn.execute(
                text("""
                    INSERT INTO unidade_saude (cnes, nome)
                    VALUES (:cnes, :nome)
                """),
                {
                    "cnes": row["CNES"],
                    "nome": row.get("NO_FANTASIA") or row.get("NO_RAZAO_SOCIAL")
                }
            )

print("✅ Importação finalizada")
