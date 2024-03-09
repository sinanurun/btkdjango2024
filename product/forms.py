from django.forms import ModelForm

from home import forms
from product.models import Comment
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']
