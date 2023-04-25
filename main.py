import pyodbc
import pandas as pd
from sql import sql as query
from config import prod


def getEstoque(query):
    conn = pyodbc.connect(prod)

    sql = pd.read_sql(query, conn)

    df = pd.DataFrame(sql, columns=['EMPRESA', 'REVENDA', 'ANOMES', 'DAATA', 'ITEM_ESTOQUE', 'ITEM_ESTOQUE_PUB', 'DES_ITEM_ESTOQUE', 'MARCA', 'GRUPO', 'CATEGORIA', 'DES_CATEGORIA', 'IDENTIFICACAO', 'UTILIZACAO_ITEM', 'DIAS_SEM_MOVIMENTO', 'DIAS_MOVIMENTO_INICIAL', 'DTA_ULT_ENTRADA', 'VAL_ESTOQUE', 'QTD_CONTABIL', 'CUSTO_MEDIO', 'QTD_PEDIDA', 'QTD_RES_OFICINA', 'QTD_NEGOCIACAO',
                      'QTD_ALOCADA', 'QTD_ORCADA', 'QTD_LITIGIO', 'QTD_TRANSITO', 'QTD_TERCEIROS', 'ORDEM_TRANSACAO', 'BASE_ICMS_RETIDO', 'QTD_CONFERENCIA', 'QTD_COMPROMETIDA', 'PRECO_CUSTO', 'PRECO_PUBLICO', 'VAL_ESTOQUE_SEM_ICMSRET', 'VAL_ICMS_RETIDO', 'DEMANDABALCAO', 'DEMANDAOFICINA', 'DEMANDATELEMARK', 'OCORRENCIAVENDAS', 'CLASS_ABC', 'CLASS_XYZ', 'TAXA_ESGOTAMENTO'])

    df = df.astype({"EMPRESA": int,
                    "REVENDA": int,
                    'ANOMES': int,
                    'DAATA': str,
                    'ITEM_ESTOQUE': int,
                    'ITEM_ESTOQUE_PUB': str,
                    'DES_ITEM_ESTOQUE': str,
                    'MARCA': str,
                    'GRUPO': int,
                    'CATEGORIA': int,
                    'DES_CATEGORIA': str,
                    'IDENTIFICACAO': str,
                    'UTILIZACAO_ITEM': str,
                    'DIAS_SEM_MOVIMENTO': int,
                    'DIAS_MOVIMENTO_INICIAL': int,
                    'DTA_ULT_ENTRADA': str,
                    'VAL_ESTOQUE': float,
                    'QTD_CONTABIL': int,
                    'CUSTO_MEDIO': float,
                    'QTD_PEDIDA': int,
                    'QTD_RES_OFICINA': int,
                    'QTD_NEGOCIACAO': int,
                    'QTD_ALOCADA': int,
                    'QTD_ORCADA': int,
                    'QTD_LITIGIO': int,
                    'QTD_TRANSITO': int,
                    'QTD_TERCEIROS': int,
                    'ORDEM_TRANSACAO': int,
                    'BASE_ICMS_RETIDO': float,
                    'QTD_CONFERENCIA': int,
                    'QTD_COMPROMETIDA': int,
                    'PRECO_CUSTO': float,
                    'PRECO_PUBLICO': float,
                    'VAL_ESTOQUE_SEM_ICMSRET': float,
                    'VAL_ICMS_RETIDO': float,
                    'DEMANDABALCAO': int,
                    'DEMANDAOFICINA': int,
                    'DEMANDATELEMARK': int,
                    'OCORRENCIAVENDAS': int,
                    'CLASS_ABC': str,
                    'CLASS_XYZ': int,
                    'TAXA_ESGOTAMENTO': float})

    df.to_csv(
        r'"\\svbi\arquivos\DW\BI Estoque\estoque_2023.csv"', index=False)


getEstoque(query=query)
