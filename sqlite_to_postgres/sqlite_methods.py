import sqlite3
from data import Data, tb_names_and_data
from loguru import logger


def process_func(row):
    if type(row) is str:
        return row.replace("'", '"') if row is not None else 'Null'
    else:
        return row if row is not None else 'Null'


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class SQLiteLoader:
    def __init__(self, sqlite_cursor: sqlite3.Connection.cursor,
                 sqlite_connect: sqlite3.Connection):
        self.cursor = sqlite_cursor
        sqlite_cursor.row_factory = dict_factory
        self.conn = sqlite_connect

    def get_data_from_table(self, table_name: str, data_class):

        sqlite_get_count_values = f"""
                                          SELECT Count(*) AS len_tb FROM {table_name}
                                          """

        sqlite_select_all_values = f"""
                                            SELECT * FROM {table_name};
                                            """

        self.cursor.execute(sqlite_get_count_values)
        limit = self.cursor.fetchone()['len_tb']

        self.conn.commit()

        self.cursor.execute(sqlite_select_all_values)

        processed_rows = (self.cursor.fetchone() for _ in range(limit))

        current_data = (data_class(**row) for row in processed_rows)

        logger.info(f"SQLite data from {table_name} was loaded")

        return current_data

    def load_movies(self, data_tb=tb_names_and_data):
        data = {tb_name: tuple(self.get_data_from_table(tb_name, data_tb[tb_name])) for tb_name in data_tb}

        return Data(**data)


