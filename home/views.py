from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    text = "BTK Django Kursu"
    # return HttpResponse("%s na Hoşgeldiniz" %text)
    context = {"text": text}
    return render(request, 'index.html', context)


def detail(request, id):
    return HttpResponse(id)