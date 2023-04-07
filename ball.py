from dal import dal
import pandas as pd

class bll:

    @classmethod
    def getIngrantes(cls) -> pd.DataFrame :
        return dal.getCategorias()

    @classmethod
    def getGastos(cls) -> pd.DataFrame:
        return dal.getGastos()

    @classmethod
    def getCategorias(cls) -> pd.DataFrame:
        return dal.getCategorias()
