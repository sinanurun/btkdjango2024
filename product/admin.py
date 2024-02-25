from django.contrib import admin

from product.models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = ['status', 'parent']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    # fields=['title','status']
    list_display = ['title', 'image', 'status']
    # list_display = ['title', 'status']
    list_filter = ['status', 'category']
    # readonly_fields = ('image_tag',)
    # inlines=[ProductImagesInline]
    prepopulated_fields = {"slug": ("title",)}  # new

admin.site.register(Product, ProductAdmin)
