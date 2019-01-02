from django.contrib import messages
from django.shortcuts import redirect

def permission_denied(request):
    messages.warning(request, '權限不足!')
    return redirect('/')