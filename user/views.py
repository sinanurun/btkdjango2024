from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from user.forms import LoginForm, RegisterForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
from user.models import UserProfile


# Create your views here.
def user_profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    context = {"user": user,
               "profile": profile}
    return render(request, 'user_profile.html', context)


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
            # tetikleme olmadan manuel profil oluşturma
            # current_user = user
            # data = UserProfile()
            # data.user_id = current_user.id
            # data.save()
            messages.success(request, "Hesabınız Oluşturuldu")
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/user/register')

    form = RegisterForm
    context = {"form": form}
    return render(request, "register.html", context)


@login_required(login_url='/user/login')  # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Kullanıcı Bilgileri Başarıyla Güncellendi")
            return HttpResponseRedirect('/user')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {"user_form": user_form, "profile_form": profile_form}
        return render(request, 'user_update.html', context)


def user_password(request):
    return None
