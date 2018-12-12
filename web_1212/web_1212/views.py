from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pow(request, x, y):
    result = x ** y
    return render(request, 'index.html', {
        'result': result
    })