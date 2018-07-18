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