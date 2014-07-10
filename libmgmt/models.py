from django.db import models

class Shelf(models.Model):
	rack_type = models.CharField(max_length=50)
	def __unicode__(self):
		return self.rack_type

class Author(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	def __unicode__(self):
		return self.name

class Publisher(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	website = models.URLField()
	def __unicode__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)
	publisher = models.ForeignKey(Publisher)
	is_available = models.BooleanField(default=True)
	book_type = models.CharField(max_length=50)
	shelf = models.ForeignKey(Shelf)
	def __unicode__(self):
		return self.title