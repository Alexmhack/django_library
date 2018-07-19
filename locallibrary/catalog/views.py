from django.shortcuts import render
from django.views import generic

from .models import Book, BookInstance, Genre, Author


def index(request):
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.count()
	num_filter_book = Book.objects.filter(author__first_name__startswith='Robert').count()
	num_genres = Genre.objects.filter('Business').count()

	context = {
		'num_books': num_books,
		'num_instances': num_instances,
		'num_instances_available': num_instances_available,
		'num_authors': num_authors,
		'num_filter_book': num_filter_book,
		'num_genres': num_genres
	}

	return render(request, 'index.html', context)


class BookListView(generic.ListView):
	model = Book
	
	# context_object_name = 'my_book_list'  # your own name for the list of books
	# queryset = Book.objects.filter(title__icontains='s')[:5]  # get 5 books with title 's'
	# template_name = 'books/book_list.html'
	
	def get_queryset(self):
		return Book.objects.filter(title__icontains='Rich')[:5]

	def get_context_data(self):
		context = super(BookListView, self).get_context_data(**kwargs)
		print(type(context))
		context['book_title'] = "Books List"
		return context


class BookDetailView(generic.ListView):
	model = Book