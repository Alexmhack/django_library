from django.contrib import admin

from .models import Book, BookInstance, Genre, Author, Language

# admin.site.register(Book)

class BookInstanceInline(admin.TabularInline):
	model = BookInstance
	extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BookInstanceInline]


# admin.site.register(Author)

class BookInline(admin.StackedInline):
	model = Book
	extra = 0


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

	inlines = [BookInline]


admin.site.register(Author, AuthorAdmin)

# admin.site.register(BookInstance)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('book', 'status', 'due_back', 'id')
	list_filter = ('status', 'due_back')

	fieldsets = (
		(None, {
			'fields': ('book', 'imprint', 'id')
		}),
		('Availability', {
			'fields': ('status', 'due_back')
		})
	)


admin.site.register(Language)
admin.site.register(Genre)