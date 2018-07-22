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

# forms url, uuid is for matching valid uuid and pk is just convention name we are catching
urlpatterns += [
	path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

# urls for author generic edit
urlpatterns += [
	path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
	path('author/<int:pk>/update', views.AuthorUpdate.as_view(), name='author_update'),
	path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]

# urls for books generic edit
urlpatterns += [
	path('book/create/', views.BookCreate.as_view(), name='book_create'),
	path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
	path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]