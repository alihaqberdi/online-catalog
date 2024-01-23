from django.contrib import admin

from product.models import Category, Product, ProductImage

# Register your models here.

admin.site.register([ProductImage])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "image", "parent"]
    list_filter = ["parent"]
    search_fields = [
        "name",
    ]
    prepopulated_fields = {"slug": ("name",)}
    autocomplete_fields = ["parent"]


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "image", "price"]
    list_display_links = ["name", "slug", "price"]
    list_filter = ["name"]
    search_fields = ["name", "category"]
    inlines = [ProductImageInline]
    prepopulated_fields = {"slug": ("name",)}
    autocomplete_fields = ["category"]
