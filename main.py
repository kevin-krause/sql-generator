import pyodbc
import pandas as pd
from sql import sql as query
from config import prod


def getEstoque(query):
    conn = pyodbc.connect(prod)

    cursor = conn.cursor().execute(query)
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    df = pd.DataFrame(results)
    print(df)

    df.to_csv(
        r"\\svbi\arquivos\DW\BI Estoque\teste_2023.csv", index=False, header=False, sep=',')


getEstoque(query=query)
