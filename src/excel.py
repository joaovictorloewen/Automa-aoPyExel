import pandas as pd

from logger import logger
from config import (
    ARQUIVO_VENDAS,
    ARQUIVO_DASHBOARD
)

def carregar_planilha():

    logger.info("Lendo planilha")

    df = pd.read_excel(ARQUIVO_VENDAS)

    return df

def limpar_dados(df):

    logger.info("Limpando dados")

    df = df.dropna()

    df = df.drop_duplicates()

    df["valor"] = df["valor"].astype(float)

    return df

def gerar_indicadores(df):

    faturamento_total = df["valor"].sum()

    ranking_vendedores = (
        df.groupby("vendedor")["valor"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    produtos_mais_vendidos = (
        df.groupby("produto")["valor"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    return (
        faturamento_total,
        ranking_vendedores,
        produtos_mais_vendidos
    )

def exportar_dashboard(df):

    logger.info("Exportando CSV")

    df.to_csv(
        ARQUIVO_DASHBOARD,
        index=False,
        sep=";"
    )