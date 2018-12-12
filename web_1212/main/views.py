from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(123)

def l(request, num1, num2):
    return render(request, 'l.html', {
        'list': range(num1, num2 + (-1 if num1 > num2 else 1), -1 if num1 > num2 else 1)
    })