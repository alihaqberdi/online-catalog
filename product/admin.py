from django.contrib import admin

from product.models import Category, Product, ProductImage

# Register your models here.

admin.site.register([Category, Product, ProductImage])
