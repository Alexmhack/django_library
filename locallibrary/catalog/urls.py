from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('books/', views.BookListView.as_view(), name='books'),
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
	path('authors/', views.AuthorListView.as_view(), name='authors'),
	path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]

# loaned books urlmapper
urlpatterns += [
	path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

# all borrowed urlmapper
urlpatterns += [
	path('borrowed/', views.AllBorrowedBookListView.as_view(), name='all-borrowed'),
]