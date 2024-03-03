from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting
from product.models import Product, Category


# Create your views here.
def index(request):
    text = "BTK Django Kursu"
    # return HttpResponse("%s na Hoşgeldiniz" %text)
    slider = Product.objects.order_by('?')[:4]
    trendy_product = Product.objects.order_by('?')[:8]
    context = {"text": text,
               "page":"home",
               "slider": slider,
               "trendy_product":trendy_product}
    return render(request, 'index.html', context)


def hakkimizda(request):
    context = {"page":"Hakkımızda"}
    return render(request, 'aboutus.html',context)

def iletisim(request):
    context = {"page":"İletişim"}
    return render(request, 'contact.html',context)

def referanslar(request):
    context = {"page":"Referanslar"}
    return render(request, 'references.html',context)