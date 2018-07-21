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

the same approach we used for the Author detail view and added Book objects for each author
in TabularInline style

We have made a templates folder inside the catalog and in there we have our base html file
index file and static folder that contains the css folder for the CSS files

We extends the index.html to base_generic.html and load our static files in base html file

The urls are not hardcoded, they are defined using the url template tag

We have used a class as a view by the as_view()

the generic from django.views has ListView with which we can just use model = Book and
it will query all the objects from DB and render a template at templates/catalog/book_list.html

within the template you can access the list of books with variable object_list or book_list

if you want your own name for accessing the objects then you can change it and also specify
your own template path

instead of just changing the queryset variable you can change the default get_queryset()

the pattern for rendering our new data along with our model is to get existing content
from superclass, then add new context information and then return the new context

For the book-detail path the URL pattern uses a special syntax to capture the specific id of 
the book that we want to see. The syntax is very simple: angle brackets define the part of the 
URL to be captured, enclosing the name of the variable that the view can use to access the capt
ured data. For example, <something> , will capture the marked pattern and pass the value 
to the view as a variable "something". You can optionally precede the variable name with a 
converter specification that defines the type of data (int, str, slug, uuid, path).

all we need to do for creating catalog/book_detail.html is pass the model = Book to 
BookDetailView

## Pagination

at the moment we have only 5 books but if we have lots of books then to display them onto
a single page will take lots of time so django has Pagination for this, just add a variable
paginate_by = int value and the objects for that View will be limited to that int value

to access page 2 you would use the URL: /catalog/books/?page=2. and so on

The same way we made the BookListView for Books we will make replicate it for Author

Below is the way through which we pass argument to the url tags
<p><strong>Author:</strong> <a href="{% url 'author-detail' book.author.pk %}">{{ book.author 
}}</a></p>

We can use the authentication urls from django framework just by adding an include in the 
root urls which we will be implemented after account/

We can set permissions for selected users on selected instances of a model by giving the 
permissions variable in meta class and then giving the permission value and the permission
display value in a tuple

** But after settings or changing anything in models.py don't forget to makemigrations and run
migrations

those permissions will be displayed in the admin page in groups and users page where we can 
select permission and move it, there the display value will appear

to use the permission in templates we use the 'perms' term with the app name and the permission
value set in the tuple

e.g. :-   
		class meta:
			permissions = (('is_library_member', 'A Library Member'))
		
		{% if perms.catalog.can_mark_returned %}code here...{% endif %}