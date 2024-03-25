from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from product.models import Category, Product


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
    items_per_page = 12
    paginator = Paginator(product_obj, items_per_page)
    page = request.GET.get("page", 1)

    try:
        obj_list = paginator.page(page)
    except PageNotAnInteger:
        obj_list = paginator.page(1)
    except EmptyPage:
        obj_list = paginator.page(paginator.num_pages)
    category_list = Category.objects.all()
    context = {"product_obj": obj_list, "category_list": category_list}
    return render(request, "product-list.html", context)


def product_detail(request, slug):
    product_obj = Product.objects.get(slug=slug)
    product_related = Product.objects.filter(category__in=product_obj.category.all()).exclude(slug=slug)
    if len(product_related) >= 4:
        product_related = product_related[:4]
    context = {"product_obj": product_obj, "product_related": product_related}
    return render(request, "product-detail.html", context)
