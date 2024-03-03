from django.forms import ModelForm, TextInput, Textarea, forms

from home.models import ContactFormMessage

class SearchForm(forms.Form):
    query = forms.CharFields()


class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(
                attrs={'type': "text", 'class': "form-control", 'id': "name", 'placeholder': "Your Name",
                       'required': "required",
                       'data-validation-required-message ': "Please enter your name"}),
            'email': TextInput(
                attrs={'type': 'email', 'class': "form-control", 'id': "email", 'placeholder': "Your Email",
                       'required': "required", 'data-validation-required-message': "Please enter your email"}),
            'subject': TextInput(
                attrs={'type': "text", 'class': "form-control", 'id': "subject", 'placeholder': "Subject",
                       'required': "required", 'data-validation-required-message': "Please enter a subject"}),
            'message': Textarea(attrs={'class': "form-control", 'rows': "6", 'id': "message", 'placeholder': "Message",
                                       'required': "required",
                                       'data-validation-required-message': "Please enter your message"}),
        }