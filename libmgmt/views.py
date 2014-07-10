from django.shortcuts import render
from django.http import HttpResponse
from libmgmt.models import Book, Shelf
from django.db.models import Q

def index(request):
	books_by_rack_type = {}
	books = Book.objects.order_by('book_type')
	for book in books:
		if book.book_type not in books_by_rack_type.keys():
			books_by_rack_type[book.book_type] = [book]
		else:
			books_by_rack_type[book.book_type].append(book)
	context = {'books_by_rack_type':books_by_rack_type}
	return render(request, 'libmgmt/index.html', context)

def searchbook(request):
	if request.method == "POST":
		title = request.POST.get("title", "")
		_type = request.POST.get("type", "")
		author = request.POST.get("author", "")
		publisher = request.POST.get("publisher", "")
		books = Book.objects.filter(Q(title__contains=title) | Q(book_type__contains=_type))
		context = {"books_found":books}
		return render(request, 'libmgmt/searchbook_results.html', context)

	if request.method == "GET":
		return render(request, "libmgmt/searchbook.html")

def bookdetail(request, book_id):
	book = Book.objects.get(id=book_id)
	context = {'book':book}
	return render(request,'libmgmt/bookdetail.html', context)

def rentbook(request, book_id):
	book = Book.objects.get(id=book_id)
	if book.is_available:
		book.is_available = False
		book.save()
		msg = "You have borrowed the book " + book.title
	else:
		msg = "The book " + book.title +" is out of stock"
	
	return HttpResponse(msg)

def returnbook(request, book_id):
	book = Book.objects.get(id=book_id)
	if not book.is_available:
		book.is_available = True
		book.save()
		msg = "You have returned the book " + book.title + ". Thank you"
	else:
		msg = "Sorry, you have not borrowed this book."
	return HttpResponse(msg)