from django.forms import ModelForm

from home.models import ContactFormMessage


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']