import sqlite3
from data import FilmWork, Genre, GenreFilmWork, Person, PersonFilmWork, Data


def process_func(row):
    if type(row) is str:
        return row.replace("'", '"') if row is not None else 'Null'
    else:
        return row if row is not None else 'Null'


class SQLiteLoader:
    def __init__(self, connection: sqlite3.Connection):
        self.conn = connection
        self.cursor = self.conn.cursor()

    def get_film_work(self):
        sqlite_select_all_values = """
                                    SELECT * FROM film_work;
                                    """

        self.cursor.execute(sqlite_select_all_values)

        processed_rows = (tuple(map(process_func, row)) for row in self.cursor.fetchall())

        film_work = (FilmWork(id=row[0],
                              title=row[1],
                              description=row[2],
                              creation_date=row[3],
                              certificate=row[4],
                              file_path=row[5],
                              rating=row[6],
                              type=row[7],
                              created_at=row[8],
                              updated_at=row[9]
                              ) for row in processed_rows)

        print("[INFO] SQLite data from film_work was loaded")
        return film_work

    def get_genre(self):
        sqlite_select_all_values = """
                                    SELECT * FROM genre;
                                    """

        self.cursor.execute(sqlite_select_all_values)

        processed_rows = (tuple(map(process_func, row)) for row in self.cursor.fetchall())

        genre = (Genre(id=row[0],
                       name=row[1],
                       description=row[2],
                       created_at=row[3],
                       updated_at=row[4],
                       ) for row in processed_rows)

        print("[INFO] SQLite data from genre was loaded")
        return genre

    def get_genre_film_work(self):
        sqlite_select_all_values = """
                                    SELECT * FROM genre_film_work;
                                    """

        self.cursor.execute(sqlite_select_all_values)

        processed_rows = (tuple(map(process_func, row)) for row in self.cursor.fetchall())

        genre_film_work = (GenreFilmWork(id=row[0],
                                         film_work_id=row[1],
                                         genre_id=row[2],
                                         created_at=row[3],
                                         ) for row in processed_rows)

        print("[INFO] SQLite data from genre_film_work was loaded")
        return genre_film_work

    def get_person(self):
        sqlite_select_all_values = """
                                    SELECT * FROM person;
                                    """

        self.cursor.execute(sqlite_select_all_values)

        processed_rows = (tuple(map(process_func, row)) for row in self.cursor.fetchall())

        person = (Person(id=row[0],
                         full_name=row[1],
                         birth_date=row[2],
                         created_at=row[3],
                         updated_at=row[4]
                         ) for row in processed_rows)

        print("[INFO] SQLite data from person was loaded")
        return person

    def get_person_film_work(self):
        sqlite_select_all_values = """
                                    SELECT * FROM person_film_work;
                                    """

        self.cursor.execute(sqlite_select_all_values)

        processed_rows = (tuple(map(process_func, row)) for row in self.cursor.fetchall())

        person_film_work = (PersonFilmWork(id=row[0],
                                           film_work_id=row[1],
                                           person_id=row[2],
                                           role=row[3],
                                           created_at=row[4]
                                           ) for row in processed_rows)

        print("[INFO] SQLite data from person_film_work was loaded")
        return person_film_work

    def load_movies(self):
        film_work = self.get_film_work()
        genre = self.get_genre()
        genre_film_work = self.get_genre_film_work()
        person = self.get_person()
        person_film_work = self.get_person_film_work()

        return Data(film_work=film_work,
                    genre=genre,
                    genre_film_work=genre_film_work,
                    person=person,
                    person_film_work=person_film_work)
