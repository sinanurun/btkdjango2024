from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from product.models import Category, Product, Images


class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 5
    readonly_fields = ['image_tag']


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = ['status', 'parent']
    prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Category, CategoryAdmin)
class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


# admin.site.register(Category,MPTTModelAdmin)
admin.site.register(Category,CategoryAdmin2)

class ProductAdmin(admin.ModelAdmin):
    # fields=['title','status']
    list_display = ['title', 'image_tag', 'status']
    # list_display = ['title', 'status']
    list_filter = ['status', 'category']
    readonly_fields = ('image_tag',)
    inlines=[ProductImagesInline]
    prepopulated_fields = {"slug": ("title",)}  # new


admin.site.register(Product, ProductAdmin)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','product', 'image_tag']
    readonly_fields = ['image_tag']
admin.site.register(Images, ImagesAdmin)
