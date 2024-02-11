from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Slug"))
    image = models.ImageField(upload_to="category", verbose_name=_("Image"))
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL, related_name="children", verbose_name=_("Parent")
    )
    product_count = models.PositiveIntegerField(default=0, verbose_name=_("Product Count"))

    def get_ancestors(self, include_self=False):
        ancestors = []
        if include_self:
            ancestors.append(self)
        parent = self.parent
        while parent:
            ancestors.append(parent)
            parent = parent.parent
        return ancestors

    def get_children(self):
        children = self.children.all()
        return children

    def __str__(self):
        return self.name


class ProductStatus(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))

    def __str__(self):
        return self.title


class Product(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Slug"))
    category = models.ManyToManyField(Category, verbose_name=_("Category"))
    image = models.ImageField(upload_to="product", verbose_name=_("Image"))
    description = models.TextField(verbose_name=_("Description"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    see_count = models.PositiveIntegerField(default=0, verbose_name=_("See Count"))
    status = models.ForeignKey(ProductStatus, on_delete=models.SET_NULL, null=True, verbose_name=_("Status"),
                               blank=True)

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name=_("Product"))
    image = models.ImageField(upload_to="product", verbose_name=_("Image"))

    def __str__(self):
        return self.product.name


class Collection(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Slug"))
    product = models.ManyToManyField(Product, verbose_name=_("Product"))

    def __str__(self):
        return self.name


class TopCategory(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Slug"), null=True)
    category = models.ManyToManyField(Category, verbose_name=_("Category"))
    image = models.ImageField(upload_to="top-category", verbose_name=_("Images"), null=True)

    def __str__(self):
        return self.name
