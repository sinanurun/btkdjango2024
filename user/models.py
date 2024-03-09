from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=1500, blank=True)
    city = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='images/users/', default='images/users/default.jpg')
    def __str__(self):
        return self.user.username
    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + '[' + self.user.username + ']'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
