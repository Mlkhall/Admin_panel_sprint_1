from django.contrib import admin
from .models import Filmwork, Genre, Person


# Register your models here.
class GenresInlineAdmin(admin.TabularInline):
    model = Filmwork.genres.through


class PersonInlineAdmin(admin.TabularInline):
    model = Filmwork.person.through

# class PersonRoleInline(admin.TabularInline):
#     model = PersonRole
#     extra = 0


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    # отображение полей в списке
    list_display = ('title', 'type', 'creation_date', 'rating',)
    # порядок следования полей в форме создания/редактирования
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

