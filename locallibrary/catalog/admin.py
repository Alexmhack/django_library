from django.contrib import admin

from .models import Book, BookInstance, Genre, Author, Language

# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	pass


# admin.site.register(Author)

class AuthorAdmin(admin.ModelAdmin):
	pass


admin.site.register(Author, AuthorAdmin)

# admin.site.register(BookInstance)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	pass


admin.site.register(Language)
admin.site.register(Genre)