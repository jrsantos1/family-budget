from config_db import conection_sqllite_3 as sqlite3
import pandas as pd

class dal:

    @classmethod
    def getIntegrantes(cls) -> pd.DataFrame:
        try:
            with sqlite3.get_connection() as con:
                query = 'select * from members'
                return pd.read_sql(sql=query, con=con)
        except Exception as e:
            print(f"Erro {e}")

    @classmethod
    def getCategorias(cls) -> pd.DataFrame:
        try:
            with sqlite3.get_connection() as con:
                query = 'select * from category'
                return pd.read_sql(sql=query, con=con)
        except Exception as e:
            print(f"Erro {e}")

    @classmethod
    def getGastos(cls) -> pd.DataFrame:
        try:
            with sqlite3.get_connection() as con:
                query = 'select * from view_expense'
                return pd.read_sql(sql=query, con=con)
        except Exception as e:
            print(f"Erro {e}")

    @classmethod
    def getSubCategoria(cls, category_id) -> pd.DataFrame:
        try:
            with sqlite3.get_connection() as con:
                query = f'select id, name from sub_category where category_id = {category_id}'
                return pd.read_sql(sql=query, con=con)
        except Exception as e:
            print(f"Erro {e}")

    @classmethod
    def inserirGasto(cls, member_id, category_id, sub_category_id, expense_date, valor, obs) -> pd.DataFrame:
        try:
            with sqlite3.get_connection() as con:
                query = f''' insert into expense (member_id, category_id, sub_category_id, expense_date, valor, obs) values ({member_id},{category_id},{sub_category_id},'{expense_date}',{valor},'{obs}')'''
                cursor = con.cursor()
                cursor.execute(query)
                con.commit()
                return True
        except Exception as e:
            con.rollback()
            print(f"Erro {e}")
            return False




