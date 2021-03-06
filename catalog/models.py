import uuid

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from datetime import date


class Genre(models.Model):
	name = models.CharField(max_length=100, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
	isbn = models.CharField('ISBN', max_length=13, help_text='13 character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	genre = models.ManyToManyField(Genre, help_text='Select a Genre for this book')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])

	def display_genre(self):
		return ', '.join([genre.name for genre in self.genre.all()])

	class Meta:
		permissions = (('is_library_member', 'A Library Member'),)

	display_genre.short_description = 'Genre'


class Language(models.Model):
	name = models.CharField(max_length=200, help_text="Enter a books's natural language (e.g. English, French, Hindi etc.)")

	def __str__(self):
		return self.name
		

class BookInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book in whole library')
	book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True, blank=True)
	language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
	borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

	LOAN_STATUS = (
		('m', 'Maintenance'),
		('o', 'On loan'),
		('a', 'Available'),
		('r', 'Reserved'),
	)

	status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book Availability')

	class Meta:
		ordering = ['due_back']
		permissions = (('is_library_member', 'A Library Member'),)

	def __str__(self):
		return '{0} ({1})'.format(self.id, self.book.title)

	@property
	def is_overdue(self):
		if self.due_back and date.today() > self.due_back:
			return True
		return False


class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	class Meta:
		ordering = ['last_name', 'first_name']
		permissions = (('is_library_member', 'A Library Member'),)

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		return f'{self.last_name} {self.first_name}'