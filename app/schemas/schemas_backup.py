from typing import Annotated
from pydantic import BaseModel , Field
from sqlalchemy import create_engine
from app.database import DATABASE_URL
from pathlib import Path
from app.schemas.user import UserBase
from uuid import UUID
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
CSV_PATH = BASE_DIR / "csv" / "cnes.csv"

engine = create_engine(DATABASE_URL)

df = pd.read_csv(CSV_PATH , low_memory = False)

conn = engine.raw_connection()

try:
    df.to_sql(
        "cnes", 
        con = conn , 
        if_exists = "append" , 
        index = False
        )
    conn.commit()
finally:
    conn.close()

print ("importação concluída")


