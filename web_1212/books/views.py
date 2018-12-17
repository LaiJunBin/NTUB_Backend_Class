from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'book.html',{
        'books': books
    })

def info(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    return render(request, 'info.html', {
        'book': book
    })

def add(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        introduction = request.POST.get('introduction')
        Book.objects.create(name=name, price=price, introduction=introduction)
        return HttpResponseRedirect('/book')