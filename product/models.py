from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


# Create your models here.
class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'))
    title = models.CharField(max_length=30)
    keywords = models.CharField(blank=True, max_length=250)
    description = models.CharField(blank=True, max_length=250)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children',
                               on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title
    class MPTTMeta:
        order_insertion_by = ['title']
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '/'.join(full_path)


class Product(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # manytoonerelationwithCategory
    title = models.CharField(max_length=150)
    keywords = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True, max_length=255)
    image = models.ImageField(blank=True, upload_to='images/', default="images/default.jpg")
    # price=models.DecimalField(max_digits=12,decimal_places=2,default=0)
    price = models.FloatField()
    amount = models.IntegerField(default=0)
    detail=RichTextUploadingField()
    # detail = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='False')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
#     urunler için resim galerisi oluşturmak için
    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')
class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'