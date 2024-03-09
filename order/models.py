from django.contrib.auth.models import User
from django.db import models

from product.models import Product


# Create your models here.
class AddFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.product.title