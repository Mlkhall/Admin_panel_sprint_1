from psycopg2.extensions import connection as _connection
from psycopg2.extras import execute_values
from loguru import logger


class PostgresSaver:
    def __init__(self, pg_conn: _connection):
        self.conn = pg_conn
        self.cursor = self.conn.cursor()

    def save_data(self, table_name, data_class):
        sql_get_columns_names = \
            f"""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name = '{table_name}';
            """

        self.cursor.execute(sql_get_columns_names)
        columns_names = tuple(map(lambda name: name[0], self.cursor.fetchall()))
        self.conn.commit()

        sql_insert_req = \
            f"""
            INSERT INTO movies_test.content.{table_name}
            {columns_names}
            VALUES %s
            ON CONFLICT (id) DO NOTHING;
            """.replace("'", '')

        inserting_rows = []
        for row_from_data_class in data_class:
            row_dict = row_from_data_class.__dict__
            adding_row = tuple((row_dict[col] for col in columns_names))
            inserting_rows.append(adding_row)

        execute_values(self.cursor, sql_insert_req, inserting_rows)
        self.conn.commit()

        logger.info(f"PostgreSQL data from {table_name} was saved")

    def save_all_data(self, data):
        data_dictionary = data.__dict__
        for tab_name in data_dictionary:
            self.save_data(table_name=tab_name, data_class=data_dictionary[tab_name])




