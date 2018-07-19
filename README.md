# django_library
local library project with django backend

# Starting project
(django_env)> django-admin startproject locallibrary

# Creating webapp
(django_env)> cd locallibrary 
(django_env)> python manage.py startapp catalog

Registering catalog application in settings.py app

Specifying the timezone to Asia/Kolkata and defining USE_TZ = False

Add urls.py from catalog to main urls.py

We are going to use only one app 'catalog' in whole project so lets redirect our root url to
our app using the RedirectView from django.views.generic in main urls.py

Django does not serve static files like CSS, JS, HTML so we need a url mapping to server static
files during development (only) using static from django.conf.urls.static at last line of 
urls.py

now let's run makemigrations and migration

now on running the server, paste the link in browser and you will be redirected to the url that
we have set and an error page occurs because we have no urls set in catalog.py

Genre model will have a name field and __str__ method

In Book model, author has ForeignKey because a author can have many books but a book can have 
only one author and, Author as a string because it has not been declared yet in the file
(in practice a book might have multiple authors, but not in this implementation!)

genre is a manytomany field because a book can have many genres and a genre can be for many 
books

you can use html in help_text argument

UUIDField is used for id field to set it as the primary_key of the model
LOAN_STATUS has key-value pairs where values will be displayed to the users with corresponding 
keys stored in the database

status has default 'm' because at first book is not in the shelves so not available, due_back
is the date when the book is expected to be returned from the borrower