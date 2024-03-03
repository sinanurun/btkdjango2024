from django.contrib import admin
from django.contrib.auth.models import User

from home.models import Setting, ContactFormMessage

# Register your models here.
admin.site.register(Setting)

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['subject','name', 'email']
admin.site.register(ContactFormMessage, ContactFormMessageAdmin)
