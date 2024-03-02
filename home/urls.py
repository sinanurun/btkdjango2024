from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # path("<int:id>", views.detail, name="detail")
   ]