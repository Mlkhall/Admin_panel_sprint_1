import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class FilmWork:
    title: str
    creation_date: Optional[datetime]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    rating: float = field(default_factory=0.0)
    certificate: str = field(default_factory='Null')
    file_path: str = field(default_factory='Null')
    type: str = field(default_factory='Null')
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    description: str = field(default_factory='Null')


@dataclass
class Genre:
    name: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    description: str = field(default_factory='Null')


@dataclass
class GenreFilmWork:
    created_at: Optional[datetime]
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    film_work_id: uuid.UUID = field(default_factory=uuid.uuid4)
    genre_id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Person:
    birth_date: Optional[datetime]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    full_name: str = field(default_factory='Null')


@dataclass
class PersonFilmWork:
    role: str
    created_at: Optional[datetime]
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    film_work_id: uuid.UUID = field(default_factory=uuid.uuid4)
    person_id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass
class Data:
    film_work: Optional
    genre: Optional
    genre_film_work: Optional
    person: Optional
    person_film_work: Optional




