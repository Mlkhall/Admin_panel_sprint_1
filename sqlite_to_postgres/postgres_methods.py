from psycopg2.extensions import connection as _connection


class PostgresSaver:
    def __init__(self, pg_conn: _connection):
        self.conn = pg_conn
        self.cursor = self.conn.cursor()

    def save_data_film_work(self, film_work):
        sql_insert_query = \
            """
            INSERT INTO movies_test.content.film_work
            (id, title, description, creation_date, certificate, file_path, rating, type, created_at, updated_at)
            VALUES ('%s', '%s', '%s', %s, %s, %s, %s, '%s', '%s', '%s')
            ON CONFLICT (id) DO NOTHING;
            """

        for row_film_work in film_work:
            adding_row = (
                row_film_work.id,
                row_film_work.title,
                row_film_work.description,
                row_film_work.creation_date,
                row_film_work.certificate,
                row_film_work.file_path,
                row_film_work.rating,
                row_film_work.type,
                row_film_work.created_at,
                row_film_work.updated_at,
            )

            self.cursor.execute(sql_insert_query % adding_row)
            self.conn.commit()

        print("[INFO] PostgreSQL data from film_work was saved")

    def save_genre(self, genre):
        sql_insert_query = \
            """
            INSERT INTO movies_test.content.genre
            (id, name, description, created_at, updated_at)
            VALUES ('%s', '%s', '%s', '%s', '%s')
            ON CONFLICT (id) DO NOTHING;
            """

        for row_genre in genre:
            adding_row = (
                row_genre.id,
                row_genre.name,
                row_genre.description,
                row_genre.created_at,
                row_genre.updated_at,
            )

            self.cursor.execute(sql_insert_query % adding_row)
            self.conn.commit()

        print("[INFO] PostgreSQL data from genre was saved")

    def save_genre_film_work(self, genre_film_work):
        sql_insert_query = \
            """
            INSERT INTO movies_test.content.genre_film_work
            (id, film_work_id, genre_id, created_at)
            VALUES ('%s', '%s', '%s', '%s')
            ON CONFLICT (id) DO NOTHING;
            """

        for row_genre_film_work in genre_film_work:
            adding_row = (
                row_genre_film_work.id,
                row_genre_film_work.film_work_id,
                row_genre_film_work.genre_id,
                row_genre_film_work.created_at,
            )

            self.cursor.execute(sql_insert_query % adding_row)
            self.conn.commit()

        print("[INFO] PostgreSQL data from row_genre_film_work was saved")

    def save_person(self, person):
        sql_insert_query = \
            """
            INSERT INTO movies_test.content.person
            (id, full_name, birth_date, created_at, updated_at)
            VALUES ('%s', '%s', %s, '%s', '%s')
            ON CONFLICT (id) DO NOTHING;
            """

        for row_person in person:
            adding_row = (
                row_person.id,
                row_person.full_name,
                row_person.birth_date,
                row_person.created_at,
                row_person.updated_at,
            )
            self.cursor.execute(sql_insert_query % adding_row)
            self.conn.commit()

        print("[INFO] PostgreSQL data from row_genre_film_work was saved")

    def save_person_film_work(self, person_film_work):
        sql_insert_query = \
            """
            INSERT INTO movies_test.content.person_film_work
            (id, film_work_id, person_id, role, created_at)
            VALUES ('%s', '%s', '%s', '%s', '%s')
            ON CONFLICT (film_work_id, person_id) DO NOTHING
            """
        for row_person_film_work in person_film_work:
            adding_row = (
                row_person_film_work.id,
                row_person_film_work.film_work_id,
                row_person_film_work.person_id,
                row_person_film_work.role,
                row_person_film_work.created_at,
            )

            self.cursor.execute(sql_insert_query % adding_row)
            self.conn.commit()

        print("[INFO] PostgreSQL data from row_genre_film_work was saved")

    def save_all_data(self, data):
        self.save_data_film_work(data.film_work)
        self.save_genre(data.genre)
        self.save_genre_film_work(data.genre_film_work)
        self.save_person(data.person)
        self.save_person_film_work(data.person_film_work)



