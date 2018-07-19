from django.shortcuts import render

from .models import Book, BookInstance, Genre, Author


def index(request):
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.count()
	num_filter_book = Book.objects.filter(title__exact='Rich Dad Poor Dad').count()
	num_genres = Genre.objects.filter(name__exact='Education').count()

	context = {
		'num_books': num_books,
		'num_instances': num_instances,
		'num_instances_available': num_instances_available,
		'num_authors': num_authors,
		'num_filter_book': num_filter_book,
		'num_genres': num_genres
	}

	return render(request, 'index.html', context)