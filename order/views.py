import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.crypto import get_random_string

from order.forms import ShopCartForm, OrderForm
from order.models import AddFavorite, ShopCart, OrderProduct, Order
from product.models import Product
from user.models import UserProfile


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
#     favori sayfasının farklı bir şekilde kullanımı
# favori_list=[]
# @login_required(login_url='/login')  # Check login
# def addfavorite(request, id):
#     url = request.META.get('HTTP_REFERER')  # get last url
#     current_user = request.user  # Access User Session information
#     product = Product.objects.get(pk=id)
#
#     checkinproduct = AddFavorite.objects.filter(product_id=id, user_id=current_user.id)  # Check product in shopcart
#     if checkinproduct:
#         messages.success(request, "urun zaten Favorilerde Mevcut")
#         return HttpResponseRedirect(url)
#     else:
#         data = AddFavorite() # model ile bağlantı kur
#         data.user_id = current_user.id
#         data.product_id = id
#         data.save()  #
#         favori_list.append(data.id)
#         json_data = json.dumps(favori_list)
#         request.session['favorite_list'] = json_data
#         request.session['favorite_items'] = AddFavorite.objects.filter(user_id=current_user.id).count()
#         messages.success(request, "Product added to Favorite")
#         return HttpResponseRedirect(url)

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

@login_required(login_url='/login')  # Check login
def deletefromcart(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    ShopCart.objects.filter(id=id).delete()
    current_user = request.user  # Access User Session information
    messages.success(request, "Your item deleted form Shopcart.")
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    return HttpResponseRedirect(url)

def orderproduct(request):
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += rs.price * rs.quantity

    if request.method == 'POST':  # if there is a post
        form = OrderForm(request.POST)
        # return HttpResponse(request.POST.items())
        if form.is_valid():
            # Send Credit card to bank,  If the bank responds ok, continue, if not, show the error
            # ..............

            data = Order()
            data.first_name = form.cleaned_data['first_name']  # get product quantity from form
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()  # random cod
            data.code = ordercode
            data.save()  #

            for rs in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id  # Order Id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.price = rs.product.price
                detail.amount = rs.amount
                detail.save()

                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()

            ShopCart.objects.filter(user_id=current_user.id).delete()  # Clear & Delete shopcart
            request.session['cart_items'] = 0
            messages.success(request, "Your Order has been completed. Thank you ")
            return render(request, 'order_completed.html', {'ordercode': ordercode})
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/orderproduct")

    user_instance = current_user
    profile = UserProfile.objects.get(user=user_instance)
    form = OrderForm()
    context = {'shopcart': shopcart,
               'total': total,
               'form': form,
               'profile': profile,
               }
    return render(request, 'order_form.html', context)



