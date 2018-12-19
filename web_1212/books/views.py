from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Book
from .forms import BookForm

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
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功!')
        return redirect('book-index')

    return render(request, 'add.html', {'form': form})
       