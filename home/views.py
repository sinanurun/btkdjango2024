from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting


# Create your views here.
def index(request):
    text = "BTK Django Kursu"
    # return HttpResponse("%s na Hoşgeldiniz" %text)
    setting = Setting.objects.get(pk=1)
    context = {"text": text,
               "page":"home",
               "setting": setting}
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {"setting": setting,
               "page":"Hakkımızda"}
    return render(request, 'aboutus.html',context)

def iletisim(request):
    setting = Setting.objects.get(pk=1)
    context = {"setting": setting,
               "page":"İletişim"}
    return render(request, 'contact.html',context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {"setting": setting,
               "page":"Referanslar"}
    return render(request, 'references.html',context)