from django.urls import path

from . import views

urlpatterns = [
   path("<int:id>/<slug:slug>", views.productDetail, name="productDetail"),
   path('addcomment/<int:id>', views.addComment, name="addComment")
   ]