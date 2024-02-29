# Dette er "keys.py"
from sqlalchemy import create_engine, URL
import os

database_host = os.environ.get("DATABASE_HOST") or "localhost"
database_password = os.environ.get("DATABASE_PASSWORD") or "Qwerty123"

# Tveit-instans, VB - SQLAlchemy:
sql_connection_string_FPT_TV_SQL01_VB = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={database_host},1433;DATABASE=master;UID=sa;PWD={database_password};Encrypt=no"

sql_connection_url_FPT_TV_SQL01_VB = URL.create(
    "mssql+pyodbc", query={"odbc_connect": sql_connection_string_FPT_TV_SQL01_VB})

sql_engine_FPT_TV_SQL01_VB = create_engine(
    sql_connection_url_FPT_TV_SQL01_VB, fast_executemany=True,echo=False)
