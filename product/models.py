from django.db import models
from common.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Category(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Slug"))
    image = models.ImageField(upload_to='category', verbose_name=_("Image"))
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children',
                               verbose_name=_("Parent"))

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Slug"))
    category = models.ManyToManyField(Category, verbose_name=_("Category"))
    image = models.ImageField(upload_to='product', verbose_name=_("Image"))
    description = models.TextField(verbose_name=_("Description"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name=_("Product"))
    image = models.ImageField(upload_to='product', verbose_name=_("Image"))

    def __str__(self):
        return self.product.name
