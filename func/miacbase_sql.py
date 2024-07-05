from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import main
from os import getenv


# файл конфигурации
main.load_dotenv(".env")
DATABASE_URL = getenv("DATABASE_URL", default="")


def base_sql(sql):
    "Делаем запросы к базе"
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    with engine.connect() as connection:
        result = connection.execute(text(sql))
        return pd.DataFrame(result.fetchall(), columns=result.keys())
