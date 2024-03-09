from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from order.models import AddFavorite
from product.models import Product


@login_required(login_url='/login')  # Check login
def addfavorite(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkinproduct = AddFavorite.objects.filter(product_id=id, user_id=current_user.id).first()
    if checkinproduct:
        checkinproduct.delete()
        messages.success(request, "urun zaten Favorilerde Mevcut")
        return HttpResponseRedirect(url)
    else:
        data = AddFavorite()
        data.product_id = id
        data.user_id = current_user.id
        data.save()
        return HttpResponseRedirect(url)
@login_required(login_url='/login')  # Check login
def favorites(request):
    current_user = request.user  # Access User Session information
    favorites = AddFavorite.objects.filter(user_id=current_user.id)
    context = {'favorites': favorites}
    return render(request, 'favorites_products.html', context)