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

BookInstance represents the specific copy of a book someone might borrow

UUIDField is used for id field to set it as the primary_key of the model
LOAN_STATUS has key-value pairs where values will be displayed to the users with corresponding 
keys stored in the database

status has default 'm' because at first book is not in the shelves so not available, due_back
is the date when the book is expected to be returned from the borrower

Author model contains the first_name last_name DOB DOD(optional) and the ordering in model, str 
representation and reverse for the author

If anybody donates some books to library of another language then for that we have a seperate
model that will have a name and __str__ method and will be used as a ForeignKey in Book model
with null=True and models.SET_NULL as we don't want to delete the objects related to it

It is recommended to have a seperate model for each object in our models.

Create the superuser using the createsuperuser command and log into the admin site

we are editing the admin models and passing our own admin classes for Author, Book and 
BookInstance, Genre and Language only have one fields so its useless for those models

we cannot directly display the genre field since it is a manytomany field so we use display_
genre to call the function display_genre in the Book model class and use it as a element in list_display tuple

we can also use list_filter to make a filter box for the elements in the tuple, those elements 
are actual names of fields in the models

The fields attribute lists just those fields that are to be displayed on the form, in order. 
Fields are displayed vertically by default, but will display horizontally if you further group 
them in a tuple (as shown in the "date" fields above).

you can add sections to group related model information within the detail form by using the
fieldset attribute

Each section has its own title and associated tuple of fields in a dictionary.

It would be very nice if we could see the BookInstance information of a particular book in
its detail view itself below the book info, to do that we can make a inline section of that
model by creating another class which inherits from admin.TabularInline and setting the model 
to BookInstance and extra = 0 so that no other BookInstances are shown except for the Book 
itself

then we can use the inlines attribute for the admin.ModelAdmin class and pass in our 
admin.TabularInline class in a list