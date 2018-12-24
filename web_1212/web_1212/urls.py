"""web_1212 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from web_1212 import views
from main import views as main

admin.site.site_title = 'Book Store Manager'
admin.site.site_header = 'Book Manager'

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
    # path('', views.index),
    # path('pow/<int:x>/<int:y>/', views.pow),
    # path('main/', main.index),
    # path('l/<int:num1>/<int:num2>/', main.l),

    path('', lambda request: redirect('book:index'), name='root'),
    path('books/', include('books.urls')),
]
