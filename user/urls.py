from django.urls import path

from user import views

urlpatterns = [
    path("", views.user_profile, name="user_profile"),
    path("login", views.user_login , name="user_login"),
    path("logout", views.user_logout, name="user_logout"),
    path("register", views.user_register, name="user_register"),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.user_password, name='user_password'),

]