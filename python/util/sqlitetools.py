"""
Functions that are useful for explore sqlite data

ref: https://stackoverflow.com/questions/305378/list-of-tables-db-schema-dump-etc-using-the-python-sqlite3-api
"""

import sqlite3
import pandas as pd


def read_data(file_path):
    """
    return (conn, c)
    """
    conn = sqlite3.connect(file_path)  # 'example.db'
    c = conn.cursor()
    return conn, c


def table_info(conn, c):
    '''
    prints out all of the columns of every table in db
    c : cursor object
    conn : database connection object
    '''
    tables = c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    for table_name in tables:
        table_name = table_name[0]  # tables is a list of single item tuples
        table = pd.read_sql_query(f"SELECT * from \"{table_name}\" LIMIT 0", conn)
        print(table_name)
        for col in table.columns:
            print('\t' + col)
        print()


def extract_tables(conn, c, table_names):
    '''
    extract either one (str) or mulitple (list) or all ([]) tables
    return either DataFrame or Dictionary
    '''
    if isinstance(table_names, str):
        table = pd.read_sql_query(f"SELECT * from \"{table_names}\"", conn)
        return table
    elif isinstance(table_names, list):
        if not table_names:
            tables = c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
            table_names = [tn[0] for tn in tables]
        tables = {}
        for table_name in table_names:
            tables[table_name] = pd.read_sql_query(f"SELECT * from \"{table_name}\"", conn)
        return tables
    else:
        assert TypeError("table_names must be either str or list or []")

# def combine_tables(conn, c, id_col):
#     '''
#     combine tables according to same id column
#     '''
