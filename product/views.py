from django.shortcuts import render

from product.models import Category, Product

# Create your views here.


def category_main(request):
    category_obj = Category.objects.filter(parent__isnull=True)
    context = {"category_obj": category_obj}
    return render(request, "category.html", context)


def category_detail(request, slug):
    category_obj = Category.objects.get(slug=slug)
    father_tree = category_obj.get_ancestors(include_self=True)

    children = category_obj.get_children()
    context = {"father_tree": father_tree[::-1], "children": children}
    return render(request, "category.html", context)


def product_list(request, slug):
    product_obj = Product.objects.filter(category__slug=slug)
    context = {"product_obj": product_obj}
    return render(request, "product-list.html", context)
