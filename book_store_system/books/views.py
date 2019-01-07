from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Book
from .forms import BookForm
from utils.forms import DeleteConfirmForm

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html',{
        'books': books
    })

def show(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/show.html', {
        'book': book
    })

@login_required
# @permission_required('books.add_book', raise_exception=True)
@permission_required('books.add_book', raise_exception=True)
def add(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, '新增成功!')
        return redirect('books:index')

    return render(request, 'books/add.html', {'form': form})
       
@login_required
@permission_required('books.change_book', raise_exception=True)
def edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        result = form.save()
        messages.success(request, '修改成功!')
        return redirect('books:show',book_id=result.id)
    return render(request, 'books/edit.html', {'form': form, 'book_id': book_id})
       
@login_required
@permission_required('books.delete_book', raise_exception=True)
def delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        book.delete()
        messages.success(request, '刪除成功!')
        return redirect('books:index')

    return render(request, 'books/delete.html', {'form': form})

def register(request):
    if(request.user.is_authenticated):
        return redirect('/')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, '{} 您好，歡迎使用～'.format(user.username))
        return redirect('root')
    
    return render(request, 'users/register.html', {
        'form': form
    })