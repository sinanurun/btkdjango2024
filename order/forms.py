from django.forms import ModelForm

from order.models import Order, ShopCart


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone', 'city', 'country']


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']
