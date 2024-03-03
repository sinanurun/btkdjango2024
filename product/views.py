from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from home.forms import SearchForm
from product.forms import CommentForm
from product.models import Category, Product, Images, Comment


# Create your views here.
def categoryProducts(request, id, slug):
    urunKategori = Category.objects.get(id=id)
    urunler = Product.objects.filter(category_id=id)


    context = {"urunKategori":urunKategori,
               "urunler":urunler}
    return render(request, 'kategori_urunler.html', context)


def productDetail(request,id,slug):
    urun = Product.objects.get(id=id)
    urun.reviewsCount = urun.reviewsCount + 1
    urun.save()
    images = Images.objects.filter(product_id=id)

    context = {"urun":urun,"images":images}
    return render(request, 'urun_detay.html', context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        print(form)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(title__icontains=query)
            context = {"urunler": results}
            return render(request, 'product_search.html',context)
    return HttpResponseRedirect('/')


def addComment(request):
    url = request.META.get('HTTP_REFERER') # geldiğimiz sayfanın url bilgisini verir
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            current_user = request.user
            data.user_id = current_user.id
            data.product = form.cleaned_data['id']
            data.save()
            messages.success(request, "yorumunuz başarıyla kaydedildi")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)