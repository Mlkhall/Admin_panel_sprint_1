from django.contrib import admin
from .models import Filmwork, Genre, Person


class GenresInlineAdmin(admin.TabularInline):
    model = Filmwork.genres.through


class PersonInlineAdmin(admin.TabularInline):
    model = Filmwork.person.through


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'creation_date', 'rating',)
    fields = (
        'title', 'type', 'description', 'creation_date', 'certificate',
        'file_path', 'rating',
    )
    inlines = (GenresInlineAdmin, PersonInlineAdmin)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    fields = ('name', 'description')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date',)
    fields = (
        'full_name', 'birth_date'
    )

