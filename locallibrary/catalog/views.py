from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Book, BookInstance, Genre, Author


def index(request):
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.count()
	num_filter_book = Book.objects.filter(author__first_name__startswith='Robert').count()
	num_genres = Genre.objects.count()
	num_visits = request.session.get('page_visits', 0)
	request.session['page_visits'] = num_visits + 1

	context = {
		'num_books': num_books,
		'num_instances': num_instances,
		'num_instances_available': num_instances_available,
		'num_authors': num_authors,
		'num_filter_book': num_filter_book,
		'num_genres': num_genres,
		'num_visits': num_visits
	}

	return render(request, 'index.html', context)


class BookListView(generic.ListView):
	model = Book
	paginate_by = 10
	
	# context_object_name = 'my_book_list'  # your own name for the list of books
	# queryset = Book.objects.filter(title__icontains='s')[:5]  # get 5 books with title 's'
	# template_name = 'books/book_list.html'
	
	def get_queryset(self):
		return Book.objects.all()[:5]

	def get_context_data(self, **kwargs):
		context = super(BookListView, self).get_context_data(**kwargs)
		context['book_title'] = "Books List"
		return context


class BookDetailView(generic.DetailView):
	model = Book


class AuthorListView(generic.ListView):
	model = Author
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super(AuthorListView, self).get_context_data(**kwargs)
		context['author_page_title'] = 'Authors List'
		return context


class AuthorDetailView(generic.DetailView):
	model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
	model = BookInstance
	template_name = 'catalog/bookinstance_list_borrowed_user.html'
	paginate_by = 10

	def get_queryset(self):
		return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
		

class AllBorrowedBookListView(PermissionRequiredMixin, generic.ListView):
	model = BookInstance
	template_name = 'catalog/all_borrowed_book_list.html'
	paginate_by = 10
	permission_required = 'catalog.is_library_member'

	def get_queryset(self):
		return BookInstance.objects.filter(status__exact='o').order_by('due_back')