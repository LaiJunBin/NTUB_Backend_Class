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
from django.urls import path, reverse_lazy
from books import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView

app_name = 'books'

login_params = {
    'template_name': 'users/login.html',
    'redirect_authenticated_user': True
}

password_reset_params = {
    'template_name': 'users/password_reset.html',
    'email_template_name': 'users/password_reset/email.html',
    'subject_template_name': 'users/password_reset/subject.txt',
    'success_url': reverse_lazy('books:login')
}

password_set_params = {
    'template_name': 'users/password_set.html',
    'post_reset_login': True,
    'success_url': reverse_lazy('books:login')
}

urlpatterns = [
    path('', views.index, name = 'index'),

    path('register', views.register,name='register'),
    path('login/', LoginView.as_view(**login_params), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', PasswordResetView.as_view(**password_reset_params), name='password_reset'),
    path('password-set/<uidb64>/<token>/', PasswordResetConfirmView.as_view(**password_set_params), name='password_set'),
    path('<int:book_id>/', views.show, name = 'show'),
    path('add', views.add, name = 'add'),
    path('edit/<int:book_id>', views.edit, name = 'edit'),
    path('delete/<int:book_id>', views.delete, name = 'delete'),
]
