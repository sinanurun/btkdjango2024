from django.shortcuts import render

from product.models import Category, Product


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
    context = {"urun":urun}
    return render(request, 'urun_detay.html', context)