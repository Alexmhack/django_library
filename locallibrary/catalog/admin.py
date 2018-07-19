from django.contrib import admin

from .models import Book, BookInstance, Genre, Author

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)