from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    # path("addtocart/<int:id>", views.addtocart, name="addtocart"),
    path("addfavorite/<int:id>", views.addfavorite, name="addfavorite"),
    path("favorites", views.favorites, name="favorites"),
    path("delfavorite/<int:id>", views.delfavorite, name="delfavorite"),
    # path("shopcart", views.shopcart, name="shopocart"),
    # path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    # path('orderproduct/', views.orderproduct, name='orderproduct'),
]