import os
import csv
from sqlalchemy import text
from app.database import engine
import uuid

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "csv", "CNES.csv")

print("📂 Lendo arquivo:", CSV_PATH)

with open(CSV_PATH, encoding="latin-1", newline="") as f:
    reader = csv.DictReader(
        f,
        delimiter=",",        
        quotechar='"'         
    )

    print("📌 Colunas reais:", reader.fieldnames[:5])  # debug rápido

    with engine.begin() as conn:
        for row in reader:
            cnes = str(row["CNES"]).strip().zfill(7)
            conn.execute(
                text("""
                    INSERT INTO unidade_saude (id ,cnes, nome)
                    VALUES (:id,:cnes, :nome)
                """),
                {
                    "id": str(uuid.uuid4()),
                    "cnes": cnes,
                    "nome": row.get("NO_FANTASIA") or row.get("NO_RAZAO_SOCIAL")
                }
            )

print("✅ Importação finalizada")
