from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse

def permission_denied(request, exception, template_name='403.html'):
    messages.warning(request, '權限不足!')
    return redirect('root')

