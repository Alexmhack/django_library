from django.db import models
from django.url import reverse


class Genre(models.Model):
	name = models.CharField(max_length=100, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

	def __str__(self):
		return self.name