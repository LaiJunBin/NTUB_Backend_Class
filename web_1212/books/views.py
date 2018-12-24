from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Book
from .forms import BookForm, DeleteConfirmForm

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
        return redirect('book:index')

    return render(request, 'add.html', {'form': form})
       
def edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        messages.success(request, '修改成功!')
        return redirect('book:index')
    return render(request, 'edit.html', {'form': form, 'book_id': book_id})
       
def delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        book.delete()
        messages.success(request, '刪除成功!')
        return redirect('book:index')

    return render(request, 'delete.html', {'form': form})

