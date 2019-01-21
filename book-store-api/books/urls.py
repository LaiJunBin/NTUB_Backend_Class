from django.contrib import admin
from django.urls import path, include
from books import views

app_name = 'books'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:book_id>/', views.show, name='show'),
    # path('add/', views.add, name='add'),
    # path('edit/<int:book_id>/', views.edit, name='edit'),
    # path('delete/<int:book_id>/', views.delete, name='delete'),

    # path('', views.index, name='list'),
    # path('<int:book_id>', views.detail, name='detail'),

]
