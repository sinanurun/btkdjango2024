from django.urls import path

from . import views

urlpatterns = [
   path("<int:id>/<slug:slug>", views.productDetail, name="productDetail"),
    # ex: /polls/
    # path("", views.index, name="index"),
    # path("<int:id>", views.detail, name="detail")
   ]