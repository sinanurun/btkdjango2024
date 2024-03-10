from django.urls import path

from user import views

urlpatterns = [
    path("", views.user_profile, name="user_profile"),
    path("login", views.user_login , name="user_login"),
    path("logout", views.user_logout, name="user_logout"),
    path("register", views.user_register, name="user_register"),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.user_password, name='user_password'),
    path('mycomments/', views.user_comments, name='user_comments'),
    path('deletecomment/<int:id>', views.user_delete_comment, name='user_delete_comment'),
    path('myorders/', views.user_orders, name='user_orders'),
    path('myorders_products/', views.user_order_product, name='user_order_product'),
    path('orderdetail/<int:id>', views.user_order_detail, name='user_order_detail'),
    path('order_product_detail/<int:id>/<int:oid>', views.user_order_product_detail, name='user_order_product_detail'),
    path('myproducts/', views.user_products, name='user_products'),
    path('user_product_add/', views.user_product_add, name='user_product_add'),
    path('delete_product/<int:id>', views.user_delete_product, name='user_delete_product'),
    path('update_product/<int:id>', views.user_update_product, name='user_update_product'),

]