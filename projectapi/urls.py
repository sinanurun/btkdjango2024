from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.list_product),
    # path('update/<int:id>', views.update_product),
    path('<int:id>', views.get_product),
    # path('list', views.list_product),
    # path('list/<int:id>', views.get_product),
    # path('create', views.create_product),
    path('delete/<int:id>', views.delete_product),
]