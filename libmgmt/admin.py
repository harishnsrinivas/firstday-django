from django.contrib import admin
from libmgmt.models import Book, Author, Publisher, Shelf

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Shelf)