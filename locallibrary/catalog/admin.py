from django.contrib import admin

from .models import Book, BookInstance, Genre, Author, Language

# admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')


# admin.site.register(Author)

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


admin.site.register(Author, AuthorAdmin)

# admin.site.register(BookInstance)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('status', 'due_back')
	list_filter = ('status', 'due_back')


admin.site.register(Language)
admin.site.register(Genre)