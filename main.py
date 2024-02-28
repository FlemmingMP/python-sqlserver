import pandas as pd
import keys

def listAllUsers():
    """
    Returnerer en liste med alle brukere i sandbox_poweroffice-databasen
    """
    query_dbs = """
    select * from brukere 
    """
    df = pd.read_sql_query(query_dbs, keys.sql_engine_FPT_TV_SQL01_VB, index_col=None)
    # Konverter til en dictionary
    dictList = df.to_dict('records')
    numberOfRecords = len(dictList)
    print(f'Got list of {numberOfRecords} users from the VB instances')
    return df.to_dict('records')

brukere = listAllUsers()

print(brukere[0]['NAVN'])