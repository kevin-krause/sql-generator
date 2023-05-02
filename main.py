import pyodbc
import pandas as pd
from sql import sql as query
import config as cfg


def returnQuery(query, dba) -> True:

<<<<<<< HEAD
    global results

    conn = pyodbc.connect(dba)
    cursor = conn.cursor().execute(query)
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    results = pd.DataFrame(results)
=======
    cursor = conn.cursor().execute(query)
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    df = pd.DataFrame(results)
    print(df)

    df.to_csv(
        r"\\svbi\arquivos\DW\BI Estoque\teste_2023.csv", index=False, header=False, sep=',')
>>>>>>> 4d83bd9079d530407840209608ac8c61dd7ad56c


def insert(table: str):

    columns = results.columns
    colunas_formatadas = []
    for i in columns:
        colunas_formatadas.append(i)
    colunas_formatadas = str(colunas_formatadas).replace(
        "'", "").replace("[", "").replace("]", "")

    valores_formatados = []
    for i, row in enumerate(results.values):
        for item in results.values[i]:
            valores_formatados.append(str(results.values[i]))

    for i, row in enumerate(valores_formatados):
        valores_formatados[i] = valores_formatados[i].replace(
            "Decimal('", "").replace("')", "").replace(",]", "]")

    insert = []
    for i in valores_formatados:

        i = str(i).replace('[', '').replace(']', '')

        sql = f'INSERT INTO {table} ({colunas_formatadas}) VALUES ({i});'
        insert.append(sql)


    with open(r'C:\Users\kevin.krause\Desktop\sankhya_dba_inc_updt_del\incert.sql', 'w') as f:
        for x in insert:
            f.write(f'{x}' + '\n')


returnQuery(query=query, dba=cfg.prodSankhya)
insert(table='TGFPRO', )
