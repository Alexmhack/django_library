from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import datetime

from .models import Book, BookInstance, Genre, Author
from .forms import RenewBookModelForm


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
		return Book.objects.all()

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


@permission_required('catalog.is_library_member')
def renew_book_librarian(request, pk):
	# we will need BookInstance object with the pk from url
	bookinst = get_object_or_404(BookInstance, pk=pk)

	# if this is a POST request then process the Form data
	if request.method == 'POST':
		# create a form instance and populate it with data from request
		form = RenewBookModelForm(request.POST)

		# check if form is valid
		if form.is_valid():
			bookinst.due_back = form.cleaned_data['renewal_date']
			bookinst.save()

			# redirect to a new url
			return HttpResponseRedirect(reverse('all-borrowed'))

	# if this is a GET or any other method then create default form
	else:
		default_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
		form = RenewBookModelForm(initial={'due_back': default_renewal_date, })

	return render(request, 'catalog/book_renewal_form.html', {'form': form, 'bookinst': bookinst})


# Author CRUD
class AuthorCreate(PermissionRequiredMixin, CreateView):
	model = Author
	fields = '__all__'
	initial = {'date_of_death': '22/07/2018'}
	permission_required = 'catalog.is_library_member'


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
	model = Author
	fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
	permission_required = 'catalog.is_library_member'


class AuthorDelete(PermissionRequiredMixin, DeleteView):
	model = Author
	success_url = reverse_lazy('authors')
	permission_required = 'catalog.is_library_member'


# Book CRUD
class BookCreate(PermissionRequiredMixin, CreateView):
	model = Book
	fields = '__all__'
	permission_required = 'catalog.is_library_member'


class BookUpdate(PermissionRequiredMixin, UpdateView):
	model = Book
	fields = '__all__'
	permission_required = 'catalog.is_library_member'


class BookDelete(PermissionRequiredMixin, DeleteView):
	model = Book
	success_url = reverse_lazy('books')
	permission_required = 'catalog.is_library_member'