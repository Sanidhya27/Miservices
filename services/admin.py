from django.contrib import admin

# Register your models here.
from services.models import Product,ProductRequest
class ProductAdmin(admin.ModelAdmin):
	list_display=['name']
class ProductRequestAdmin(admin.ModelAdmin):
	list_display=['Department','quantityname','quantitydemanded','quantitysupplied']
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductRequest,ProductRequestAdmin)

