import pyodbc
import pandas as pd
from sql import sql as query
from config import prod


def getEstoque(query):
    conn = pyodbc.connect(prod)

    sql = pd.read_sql(query, conn)

    df = pd.DataFrame(sql, columns=['EMPRESA', 'REVENDA', 'ANOMES', 'DAATA', 'ITEM_ESTOQUE', 'ITEM_ESTOQUE_PUB', 'DES_ITEM_ESTOQUE', 'MARCA', 'GRUPO', 'CATEGORIA', 'DES_CATEGORIA', 'IDENTIFICACAO', 'UTILIZACAO_ITEM', 'DIAS_SEM_MOVIMENTO', 'DIAS_MOVIMENTO_INICIAL', 'DTA_ULT_ENTRADA', 'VAL_ESTOQUE', 'QTD_CONTABIL', 'CUSTO_MEDIO', 'QTD_PEDIDA', 'QTD_RES_OFICINA', 'QTD_NEGOCIACAO',
                      'QTD_ALOCADA', 'QTD_ORCADA', 'QTD_LITIGIO', 'QTD_TRANSITO', 'QTD_TERCEIROS', 'ORDEM_TRANSACAO', 'BASE_ICMS_RETIDO', 'QTD_CONFERENCIA', 'QTD_COMPROMETIDA', 'PRECO_CUSTO', 'PRECO_PUBLICO', 'VAL_ESTOQUE_SEM_ICMSRET', 'VAL_ICMS_RETIDO', 'DEMANDABALCAO', 'DEMANDAOFICINA', 'DEMANDATELEMARK', 'OCORRENCIAVENDAS', 'CLASS_ABC', 'CLASS_XYZ', 'TAXA_ESGOTAMENTO'])

    df.to_csv(r'C:\Users\kevin.krause\Desktop\estoque_apollo\estoque_2023.csv')


getEstoque(query=query)
