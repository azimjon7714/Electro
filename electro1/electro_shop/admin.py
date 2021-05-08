from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

    class Meta:
        model: Category

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

    class Meta:
        model: Brand

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

    class Meta:
        model: Product

admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(TestProduct)
admin.site.register(Gallery)
admin.site.register(Photo)
admin.site.register(CartItem)
admin.site.register(Cart)
