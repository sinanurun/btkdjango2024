from django.forms import ModelForm
from product.models import Comment
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']