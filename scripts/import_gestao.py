from sqlalchemy import text
from app.database import engine
from pathlib import Path
import csv

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
                text("""INSERT INTO gestao(
                     tipo_gestao,
                     esfera_admin,
                     retencao,
                     unidade_id
                     )VALUES (
                     :tp_gestao,
                     :admin,
                     :retencao,
                     :unidade_id
                     )"""),
                     {
                         "tp_gestao": row["TPGESTAO"],
                         "admin": row.get("ESFERA_A"),
                         "retencao": row.get("RETENCAO"),
                         "unidade_id": unidade.id
                     }
            )
print("LOCATION importado corretamente")
