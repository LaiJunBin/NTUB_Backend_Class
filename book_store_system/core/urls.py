"""core URL Configuration

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
from django.contrib.auth.views import LoginView, LogoutView

from .views import permission_denied

login_params = {
    'template_name': 'users/login.html',
    'redirect_authenticated_user': True
}

# logout_params = {
#     'next_page': '/'
# }

urlpatterns = [
    path('', lambda request: redirect('books:index'), name='root'),
    path('login/', LoginView.as_view(**login_params), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('jet/', include('jet.urls', 'jet'), 'jet'),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('403/', permission_denied, name='403'),
]
