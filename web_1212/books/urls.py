from django.urls import path
from books import views as book


app_name = 'book'

urlpatterns = [
    path('', book.index, name = 'index'),
    path('<int:book_id>/', book.info, name = 'info'),
    path('add', book.add, name = 'add'),
    path('edit/<int:book_id>', book.edit, name = 'edit'),
    path('delete/<int:book_id>', book.delete, name = 'delete'),
]
