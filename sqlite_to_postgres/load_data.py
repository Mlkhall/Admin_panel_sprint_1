import os
import sqlite3
import psycopg2
import traceback

from dotenv import load_dotenv
from contextlib import closing
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor
from sqlite_methods import SQLiteLoader
from postgres_methods import PostgresSaver
from loguru import logger


def load_from_sqlite(pg_conn: _connection, **sqlite_params):
    """Основной метод загрузки данных из SQLite в Postgres"""
    postgres_saver = PostgresSaver(pg_conn)
    sqlite_loader = SQLiteLoader(**sqlite_params)

    data = sqlite_loader.load_movies()
    postgres_saver.save_all_data(data)


if __name__ == '__main__':
    logger.add('./logs/logs.log', level='DEBUG')
    if load_dotenv('./.env'):
        logger.info('Переменные окружения загружены')

    dsl = {'dbname': os.environ.get('DB_NAME', 'some_db'),
           'user': os.environ.get('DB_USER', 'defult_user'),
           'password': os.environ.get('PASSWORD'),
           'host': os.environ.get('HOST', '127.0.0.1'),
           'port': os.environ.get('PORT', 5432)}

    pg_conn = psycopg2.connect(**dsl, cursor_factory=DictCursor)
    try:
        with sqlite3.connect('db.sqlite') as sqlite_conn:

            with closing(sqlite_conn.cursor()) as cursor:
                sqlite_args = dict(sqlite_cursor=cursor,
                                   sqlite_connect=sqlite_conn)
                load_from_sqlite(pg_conn, **sqlite_args)

    except Exception as ex:
        logger.error(f'ERROR: {ex}\n{traceback.print_exc()}')

    finally:
        if pg_conn:
            pg_conn.close()




