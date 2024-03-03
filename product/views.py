from django.shortcuts import render

from product.models import Category, Product


# Create your views here.
def categoryProducts(request, id, slug):
    urunKategori = Category.objects.get(id=id)
    urunler = Product.objects.get(category_id=id)

    context = {"urunKategori":urunKategori,
               "urunler":urunler}
    return render(request, 'kategori_urunler.html', context)