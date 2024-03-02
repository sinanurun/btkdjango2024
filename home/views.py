from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting


# Create your views here.
def index(request):
    text = "BTK Django Kursu"
    # return HttpResponse("%s na Hoşgeldiniz" %text)
    setting = Setting.objects.get(pk=1)
    context = {"text": text,
               "setting": setting}
    return render(request, 'index.html', context)


def detail(request, id):
    return HttpResponse(id)