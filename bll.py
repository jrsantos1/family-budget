from dal import dal
import pandas as pd

class bll:

    @classmethod
    def getIngrantes(cls) -> pd.DataFrame:
        dados = dal.getIntegrantes()
        dados.rename(columns={'id': 'value', 'name': 'label'}, inplace=True)
        return dados.to_dict(orient='records')

    @classmethod
    def getGastos(cls) -> pd.DataFrame:
        dados =  dal.getGastos()
        dados.rename(columns={'id': 'value', 'name': 'label'}, inplace=True)
        return dados.to_dict(orient='records')

    @classmethod
    def getCategorias(cls) -> pd.DataFrame:
        dados = dal.getCategorias()
        dados.rename(columns={'id': 'value', 'name': 'label'}, inplace=True)
        return dados.to_dict(orient='records')

    @classmethod
    def getSubCategoriaByCategoryId(cls, category_id):
        dados = dal.getSubCategoria(category_id=category_id)
        dados.rename(columns={'id': 'value', 'name': 'label'}, inplace=True)
        return dados.to_dict(orient='records')

    @classmethod
    def inserirGasto(cls, member_id, category_id, sub_category_id, expense_date, valor, obs):
        dal.inserirGasto(member_id, category_id, sub_category_id, expense_date, valor, obs)



