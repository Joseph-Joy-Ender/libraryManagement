from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'ISBN', 'list_genre']
    list_per_page = 10
    list_filter = ['title']
    search_fields = ['title', 'ISBN']
    ordering = ['title']


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth']


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

# admin.site.register(models.Book, BookAdmin)
# admin.site.register(models.Genre)
# admin.site.register(models.Author)
