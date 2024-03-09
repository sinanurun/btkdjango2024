from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def user_profile(request):
    return HttpResponse("<h1>User Profile</h1>")


def user_login(request):
    pass


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")



def user_register(request):
    pass