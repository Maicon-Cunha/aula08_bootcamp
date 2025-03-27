import pandas as pd
import os
import glob

# uma funcao de extract que le e consolida json


def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# uma funcao que transforma

def calcular_kpi_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# uma funcao que da load em csv ou parquet

def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    parametro que vai ser ou "csv" ou "parquet" ou "os dois"
    """
    print(format_saida)
    for formato in format_saida:
        if formato == "csv":
            df.to_csv("dados.csv")
        if formato == "parquet":
            df.to_parquet("dados.parquet")


    if __name__ == "__main__":
        pasta_argumento = "data"
        data_frame = extrair_dados_e_consolidar(pasta=pasta_argumento)
        print(calcular_kpi_vendas(data_frame))