from django.contrib import admin

from .models import Book, BookInstance, Genre, Author, Language

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)