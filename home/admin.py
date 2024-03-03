from django.contrib import admin
from django.contrib.auth.models import User

from home.models import Setting, ContactFormMessage

# Register your models here.
admin.site.register(Setting)

admin.site.register(ContactFormMessage)
