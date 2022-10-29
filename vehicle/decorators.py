from django.http import HttpResponse
from django.shortcuts import redirect


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.is_superuser:
            return redirect('list')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper_function