from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.text import slugify

from order.models import Order, OrderProduct
from product.models import Comment, Product
from user.forms import LoginForm, RegisterForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm, ProductForm
from user.models import UserProfile


# Create your views here.
def user_profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    context = {"user": user,
               "profile": profile}
    return render(request, 'user_profile.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Başarılı Şekilde Oturum Açtınız'.format(user.username))
                return HttpResponseRedirect('/user/login')
            else:
                messages.warning(request, 'Tekrar Oturum Açmayı Deneyiniz')
                return HttpResponseRedirect('/user/login')

    form = LoginForm
    context = {"form": form}
    return render(request, "login.html", context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            # tetikleme olmadan manuel profil oluşturma
            # current_user = user
            # data = UserProfile()
            # data.user_id = current_user.id
            # data.save()
            messages.success(request, "Hesabınız Oluşturuldu")
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/user/register')

    form = RegisterForm
    context = {"form": form}
    return render(request, "register.html", context)


@login_required(login_url='/user/login')  # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Kullanıcı Bilgileri Başarıyla Güncellendi")
            return HttpResponseRedirect('/user')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {"user_form": user_form, "profile_form": profile_form}
        return render(request, 'user_update.html', context)


@login_required(login_url='/user/login')
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'user_password_update.html', {'form': form})


@login_required(login_url='/user/login')
def user_comments(request):
    comments = Comment.objects.filter(user=request.user)
    return render(request, 'user_comments.html', {'comments': comments})


@login_required(login_url='/user/login')
def user_delete_comment(request, id):
    current_user = request.user
    try:
        Comment.objects.filter(id=id, user_id=current_user.id).delete()
        messages.success(request, 'Mesajınız Başarıyla Silinmiştir')
    except Exception:
        messages.warning(request, 'Mesajınız Silinememiştir {}'.format(Exception))
    return HttpResponseRedirect('/user/mycomments')


@login_required(login_url='/login')  # Check login
def user_orders(request):
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)
    context = {'orders': orders, }
    return render(request, 'user_orders.html', context)


@login_required(login_url='/login')  # Check login
def user_order_detail(request, id):
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    context = {'order': order, 'orderitems': orderitems}
    return render(request, 'user_order_detail.html', context)


@login_required(login_url='/login')  # Check login
def user_order_product(request):
    current_user = request.user
    order_product = OrderProduct.objects.filter(user_id=current_user.id).order_by('-id')
    context = {'order_product': order_product}
    return render(request, 'user_order_products.html', context)


@login_required(login_url='/login')  # Check login
def user_order_product_detail(request, id, oid):
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=oid)
    orderitems = OrderProduct.objects.filter(id=id, user_id=current_user.id)
    context = {'order': order, 'orderitems': orderitems, }
    return render(request, 'user_order_detail.html', context)


@login_required(login_url='/login')  # Check login
def user_products(request):
    current_user = request.user
    products = Product.objects.filter(user_id=current_user.id)
    context = {'products': products, }
    return render(request, 'user_products.html', context)


@login_required(login_url='/login')  # Check login
def user_product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Product()
            data.user_id = current_user.id
            data.title = form.cleaned_data['title']
            data.detail = form.cleaned_data['detail']
            data.category = form.cleaned_data['category']
            data.price = form.cleaned_data['price']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            # sonid = Product.objects.last().id
            # data.slug = slugify(str(sonid+1)+"_"+form.cleaned_data['title'])
            data.save()
            messages.success(request, "Your Product is Added")
            return HttpResponseRedirect('/user/myproducts')
        else:
            messages.success(request, "Product Form Error : " + str(form.errors))
            return HttpResponseRedirect('/user/myproducts')

    form = ProductForm
    current_user = request.user
    products = Product.objects.filter(user_id=current_user.id)
    context = {
        'products': products,
        'form': form }
    return render(request, 'user_products_add.html', context)


@login_required(login_url='/login')  # Check login
def user_delete_product(request, id):
    current_user = request.user
    Product.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Ürününüz deleted..')
    return HttpResponseRedirect('/user/products')

#
# #
# #
@login_required(login_url='/login')  # Check login
def user_update_product(request, id):
    pass
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Product ise Updateded")
            return HttpResponseRedirect('/user/myproducts')
        else:
            messages.success(request, "Poruduct Form Error : " + str(form.errors))
            return HttpResponseRedirect('/user/myproducts')

    form = ProductForm(instance=product)

    current_user = request.user
    product = Product.objects.get(pk=id)
    context = {
               'product': product,
               'form': form,
               }
    return render(request, 'user_products_update.html', context)

