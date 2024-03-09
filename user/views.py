from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from product.models import Comment
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
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
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


@login_required(login_url='/user/login')
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'user_password_update.html', {'form': form})


@login_required(login_url='/user/login')
def user_comments(request):
    comments = Comment.objects.filter(user=request.user)
    return render(request, 'user_comments.html', {'comments': comments})


@login_required(login_url='/user/login')
def user_deletecomment(request, id):
    current_user = request.user
    try:
        Comment.objects.filter(id=id, user_id=current_user.id).delete()
        messages.success(request, 'Mesajınız Başarıyla Silinmiştir')
    except Exception:
        messages.warning(request, 'Mesajınız Silinememiştir {}'.format(Exception))
    return HttpResponseRedirect('/user/mycomments')
