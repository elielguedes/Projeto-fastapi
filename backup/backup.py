from sqlalchemy import create_engine
from datetime import datetime
from app.database import DATABASE_URL , engine
import sqlite3
import os

# ==== Pasta do backup
PASTA_BACKUP = r"C:\backups_sqlite"


os.makedirs(PASTA_BACKUP , exist_ok = True)

def BackupBanco():
    data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    caminho = os.path.join(PASTA_BACKUP , f"backup_{data}.db")

    origin = engine.raw_connection()
    dest = sqlite3.connect(f"backup_{data}.db")

    origin.backup(dest)

    dest.close()
    origin.close()

    print("### BACKUP SCRIPT CARREGADO ###")

# ==== Inicializa o scripts =====
if __name__ == "__main__":
    BackupBanco()
