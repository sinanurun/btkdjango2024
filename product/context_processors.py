from .models import Category
def category(request):
    category = Category.objects.all()
    if category:
        return {'category': category}