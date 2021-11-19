import uuid

from django.db import models
from django.db.models import UniqueConstraint, Q
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(TimeStampedModel):
    id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(_('Полное Имя'), max_length=50)
    birth_date = models.DateField(_('Дата Рождения'), blank=True)

    class Meta:
        verbose_name = _('Персона')
        verbose_name_plural = _('Персоны')
        db_table = "content\".\"person"

    def __str__(self):
        return self.full_name


class Genre(TimeStampedModel):
    id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('Название'), max_length=255)
    description = models.TextField(_('Описание'), blank=True)

    class Meta:
        verbose_name = _('Жанр')
        verbose_name_plural = _('Жанры')
        db_table = "content\".\"genre"

    def __str__(self):
        return self.name


class FilmworkGenre(models.Model):
    id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False)
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"


class PersonRole(models.TextChoices):
    DIRECTOR = 'director', _('Директор')
    WRITER = 'writer', _('Сценарист')
    ACTOR = 'actor', _('Актер')


class PersonFilmWork(models.Model):
    id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False)
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    role = models.CharField(_('Роль'),  max_length=20, choices=PersonRole.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Персона')
        verbose_name_plural = _('Лица')
        db_table = "content\".\"person_film_work"
        constraints = [
            UniqueConstraint(
                fields=['id', 'film_work_id', 'person_id'],
                name="film_work_person"),
            UniqueConstraint(
                fields=['id'],
                name="person_film_work_pkey")
        ]

    def __str__(self):
        return 'Личность'


class FilmworkType(models.TextChoices):
    MOVIE = 'movie', _('Фильм')
    TV_SHOW = 'tv_show', _('ТВ Шоу')


class Filmwork(TimeStampedModel):
    id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_('Название'), max_length=255)
    description = models.TextField(_('Описание'), blank=True)
    creation_date = models.DateField(_('Дата создания'), blank=True)
    certificate = models.TextField(_('Сертификат'), blank=True)
    file_path = models.FileField(_('Файл'), upload_to='film_works/', blank=True)
    rating = models.FloatField(_('Рэйтинг'), validators=[MinValueValidator(0), MaxValueValidator(10)], blank=True)
    type = models.CharField(_('Тип'), max_length=20, choices=FilmworkType.choices)

    genres = models.ManyToManyField(Genre, through='FilmworkGenre')
    person = models.ManyToManyField(Person, through='PersonFilmWork')

    class Meta:
        verbose_name = _('Кинопроизведение')
        verbose_name_plural = _('Кинопроизведения')
        db_table = "content\".\"film_work"

    def __str__(self):
        return f'Фильм {self.title}'



