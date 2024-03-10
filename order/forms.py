from django.contrib.auth.models import User
from django.forms import ModelForm, forms
from order.models import Order, ShopCart
from user.forms import UserProfileForm
from user.models import UserProfile


# class UserForm2(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name','email']
#
# class UserProfileForm2(ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['phone_number', 'address', 'city', 'country']

class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone', 'city', 'country']

 # def __init__(self, *args, **kwargs):
 #        super(OrderForm, self).__init__(*args, **kwargs)
 #        self.fields.update(UserForm2().fields)
 #        self.fields.update(UserProfileForm2().fields)


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']
