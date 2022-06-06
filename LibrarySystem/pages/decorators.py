from django import http
from django.http import HttpResponse
from django.shortcuts import redirect


def req_Login(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('student')

        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorate(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
        
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed!')
        
        return wrapper_func
    return decorate