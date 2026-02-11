from ..database import engine

def load_to_db(dataframes: dict):
    for table_name , df in dataframes.items():
        df.to_sql(
            name = table_name,
            con = engine,
            if_exists = "replace",
            index = False
        )