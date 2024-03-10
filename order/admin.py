from django.contrib import admin

from order.models import AddFavorite, Order, OrderProduct, ShopCart


# Register your models here.
class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity','price','amount' ]
    list_filter = ['user']

class FavoriteProductsAdmin(admin.ModelAdmin):
    list_display = ['product','user']
    list_filter = ['user']


class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product','price','quantity','amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','phone','city','total','status']
    list_filter = ['status']
    readonly_fields = ('user','address','city','country','phone','first_name','ip', 'last_name','phone','city','total')
    can_delete = False
    inlines = [OrderProductline]

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','price','quantity','amount']
    list_filter = ['user']

# Register your models here.
admin.site.register(AddFavorite)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(ShopCart)