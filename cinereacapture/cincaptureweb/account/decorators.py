from django.http import HttpResponse
from django.shortcuts import render, redirect
from account.settings import get_user_navLinks

def views_allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.usergrouptypes.lower() != None :
                group = request.user.usergrouptypes.lower()
                print (group)
                print(allowed_roles)
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                context = {}
               # return HttpResponse('You are not allowed')
                context['navlinks'] = get_user_navLinks(request)
                return render(request, "personal/forbidden.html", context)
        return wrapper_func
    return decorator

