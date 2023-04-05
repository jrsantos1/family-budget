from config_db import conection_sqllite_3 as sqlite3
import pandas as pd

class dal:

    @classmethod
    def getIntegrantes(cls) -> pd.DataFrame:
        try:
            with sqlite3.get_connection() as con:
                query = 'select * from members'
                dados = pd.read_sql(sql=query, con=con).to_dict(orient='records')
                return dados
        except Exception as e:
            print(f"Erro {e}")

    @classmethod
    def getCategorias(cls) -> pd.DataFrame:
        try:
            with sqlite3.get_connection() as con:
                query = 'select * from expense_category'
                dados = pd.read_sql(sql=query, con=con).to_dict(orient='records')
                return dados
        except Exception as e:
            print(f"Erro {e}")

    @classmethod
    def getGastos(cls) -> pd.DataFrame:
        try:
            with sqlite3.get_connection() as con:
                query = 'select * from expense'
                dados = pd.read_sql(sql=query, con=con).to_dict(orient='records')
                return dados
        except Exception as e:
            print(f"Erro {e}")


