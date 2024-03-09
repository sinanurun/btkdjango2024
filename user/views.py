from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from user.forms import LoginForm, RegisterForm


# Create your views here.
def user_profile(request):
    return HttpResponse("<h1>User Profbnbile</h1>")


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Başarılı Şekilde Oturum Açtınız'.format(user.username))
                return HttpResponseRedirect('/user/login')
            else:
                messages.warning(request, 'Tekrar Oturum Açmayı Deneyiniz')
                return HttpResponseRedirect('/user/login')

    form = LoginForm
    context = {"form": form}
    return render(request, "login.html", context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"Hesabınız Oluşturuldu")
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/user/register')

    form = RegisterForm
    context = {"form": form}
    return render(request, "register.html", context)
