from django.contrib import admin
from product.models import Category,Product,SubCategory
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Product)