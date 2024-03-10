from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from order.forms import ShopCartForm
from order.models import AddFavorite, ShopCart
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

@login_required(login_url='/login')  # Check login
def delfavorite(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    AddFavorite.objects.filter(product_id=id, user_id=current_user.id).delete()
    return HttpResponseRedirect(url)

@login_required(login_url='/login')  # Check login
def addtocart(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information
    product = Product.objects.get(pk=id)

    checkinproduct = ShopCart.objects.filter(product_id=id, user_id=current_user.id)  # Check product in shopcart
    if checkinproduct:
        control = 1  # The product is in the cart
    else:
        control = 0  # The product is not in the cart"""

    if request.method == 'POST':  # if there is a post
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:  # Update  shopcart
                data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()  # save data
            else:  # Inser to Shopcart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Product added to Shopcart ")
        request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
        return HttpResponseRedirect(url)

    else:  # if there is no post
        if control == 1:  # Update  shopcart
            data = ShopCart.objects.get(product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()  #
        else:  # Inser to Shopcart
            data = ShopCart()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()  #
        request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
        messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)

def shopcart(request):
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += rs.product.price * rs.quantity
    #     print(total)
    # # return HttpResponse(str(total))
    context = {'shopcart': shopcart,
               'total': total,
               }
    return render(request, 'shopcart_products.html', context)

