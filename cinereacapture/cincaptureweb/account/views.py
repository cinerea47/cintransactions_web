from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from account.settings import get_user_navLinks
from account.constants import SUPERVISOR_ACC, TELLER_ACC

from account.models import Account


@login_required(login_url='/login')
def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:  #GET request
        form = RegistrationForm()
        context['registration_form'] = form
        context['navlinks'] = get_user_navLinks(request)
        context['defaultgroupuser'] = get_user_grouptype(request)
    return render(request, 'account/register.html', context)


@login_required(login_url='/login')
def registration_teller(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            Account.objects.filter(id=user_instance.id).update(
                usergrouptypes=TELLER_ACC
            )
            return redirect('home')
        else:
            context['registration_form'] = form
    else:  #GET request
        form = RegistrationForm()
        context['registration_form'] = form
        context['navlinks'] = get_user_navLinks(request)
        context['register_title'] = "Register Teller"
    return render(request, 'account/register.html', context)


@login_required(login_url='/login')
def registration_supervisor(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            Account.objects.filter(id=user_instance.id).update(
                usergrouptypes=SUPERVISOR_ACC
            )
            return redirect('home')
        else:
            context['registration_form'] = form
    else:  #GET request
        form = RegistrationForm()
        context['registration_form'] = form
        context['navlinks'] = get_user_navLinks(request)
        context['register_title'] = "Register Supervisor"
    return render(request, 'account/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                print(user.usergrouptypes)
                if user.usergrouptypes == TELLER_ACC:
                    logout(request)
                    return redirect ("denied")
                return redirect("home")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    # print(form)
    return render(request, "account/login.html", context)


@login_required(login_url='/login')
def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:  #GET request
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
                "firstname": request.user.firstname,
                "lastname": request.user.lastname,
            }
        )
        context['account_form'] = form
        context['navlinks'] = get_user_navLinks(request)
    return render(request, 'account/account.html', context)


def get_user_grouptype(request):
    if (request.user.usergrouptypes == SUPERVISOR_ACC):
        print("Supervisor User returned")
        return SUPERVISOR_ACC
    else:
        return TELLER_ACC
