from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from product.models import Category, Collection, Product, TopCategory


def main_page(request):
    collection = Collection.objects.filter(is_active=True).prefetch_related("product")
    all_collection_product = Product.objects.filter(id__in=collection.values_list("product", flat=True))
    if len(all_collection_product) > 12:
        all_collection_product = all_collection_product[:12]
    category = TopCategory.objects.first()
    all_category = Category.objects.filter(is_active=True).prefetch_related("product_set")
    default_category = all_category.first()
    products = Product.objects.filter(is_active=True)
    obj_list = []
    if default_category:
        items_per_page = 12
        paginator = Paginator(default_category.product_set.all(), items_per_page)
        page = request.GET.get("page", 1)

        try:
            obj_list = paginator.page(page)
        except PageNotAnInteger:
            obj_list = paginator.page(1)
        except EmptyPage:
            obj_list = paginator.page(paginator.num_pages)

    context = {
        "category": category.category.all()[1:] if category else None,
        "default_category": category.category.first() if category else None,
        "all_category": all_category,
        "obj_list": obj_list,
        "product_obj": products,
    }
    return render(request, "index.html", context)


def search(request):
    q = request.GET.get("q")
    product_obj = Product.objects.filter(name__icontains=q)
    category_list = Category.objects.all()
    context = {"product_obj": product_obj, "category_list": category_list, "q": q}
    return render(request, "product-list.html", context)
