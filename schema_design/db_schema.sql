-- Создание отдельной схемы для контента:
CREATE SCHEMA IF NOT EXISTS content;

-- Кинопроизведения:
CREATE TABLE IF NOT EXISTS content.film_work
(
    id uuid PRIMARY KEY ,
    title TEXT NOT NULL ,
    description TEXT,
    creation_date DATE,
    certificate TEXT,
    file_path TEXT,
    rating FLOAT DEFAULT 0,
    type TEXT not null,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- Жанры кинопроизведений:
CREATE TABLE IF NOT EXISTS content.genre
(
    id uuid PRIMARY KEY ,
    name TEXT NOT NULL ,
    description TEXT,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- Жанры в кинопроизведениях:
CREATE TABLE IF NOT EXISTS content.genre_film_work
(
    id uuid PRIMARY KEY ,
    film_work_id uuid NOT NULL,
    genre_id uuid NOT NULL,
    created_at timestamp with time zone
);

-- Актеры:
CREATE TABLE IF NOT EXISTS content.person
(
    id uuid PRIMARY KEY ,
    full_name TEXT NOT NULL,
    birth_date DATE,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- Актеры в кинопроизведениях:
CREATE TABLE IF NOT EXISTS content.person_film_work
(
    id uuid PRIMARY KEY ,
    film_work_id uuid NOT NULL,
    person_id uuid NOT NULL,
    role TEXT NOT NULL,
    created_at timestamp with time zone
);

-- Создадим уникальный композитный индекс film_work_person для таблицы person_film_work так,
-- чтобы нельзя было добавить одного актёра несколько раз к одному фильму.
CREATE UNIQUE INDEX film_work_person ON content.person_film_work (film_work_id, person_id);
