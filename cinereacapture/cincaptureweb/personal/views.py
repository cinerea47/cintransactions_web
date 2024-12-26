from django.shortcuts import render, loader
from django.http import HttpResponse
from account.models import Account
from account.settings import get_user_navLinks

def home_screen_view(request):

    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    context['navlinks'] = get_user_navLinks(request)


    return render(request, "personal/home.html", context)

def construction_screen_view(request):

    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    context['navlinks'] = get_user_navLinks(request)


    return render(request, "personal/underconstruction.html", context)
def forbidden_screen_view(request):

    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    context['navlinks'] = get_user_navLinks(request)


    return render(request, "personal/forbidden.html", context)

    #METHOD 2
   # template = loader.get_template('personal/home.html')

    #return HttpResponse(template.render(context))

def update_msg_view(request):
    context = {}
    context['message'] = request.GET.get("message")
    print("context mesage = "+context['message'])
    context['navlinks'] = get_user_navLinks(request)
    return render(request, "personal/updated.html", context)