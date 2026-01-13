from sqlalchemy import text
from app.database import engine 
from pathlib import Path
import csv

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "csv" / "cnes.csv"

with engine.begin() as conn:
    with open(CSV_PATH , newline = "" , encoding = "latin-1") as csvfile:
        reader = csv.DictReader(csvfile)

        print("Colunas reais: ", reader.fieldnames)

        for row in reader:
            unidade = conn.execute(
                text("SELECT id FROM unidade_saude WHERE cnes = :cnes"),
                {"cnes": row["CNES"]}
            ).fetchone()

            if not unidade:
                continue
            total = (
                int(row.get("QTLEITP1") or 0),
                int(row.get("QTLEITP2") or 0),
                int(row.get("QTLEITP3") or 0),

            )

            conn.execute(text(
                """INSERT INTO leitos (
                 leitos_tipo_1,
                 leitos_tipo_2,
                 leitos_tipo_3,
                 total_leitos,
                 unidade_id
                )VALUES (
                 :l1,
                 :l2,
                 :l3,
                 :total,
                 :unidade_id
                ) 
                """),
                {
                    "leitos_1": row["QTLEITP1"] or 0,
                    "leitos_2": row["QTLEITP2"] or 0,
                    "leitos_3": row["QTLEITP3"] or 0,
                    "total": total,
                    "unidade_id": unidade.id
                }
                
            )

print("location importado com sucesso")