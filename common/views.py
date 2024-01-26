from django.shortcuts import render

from product.models import Category, Collection, Product, TopCategory


def main_page(request):
    collection = Collection.objects.filter(is_active=True).prefetch_related("product")
    all_collection_product = Product.objects.filter(id__in=collection.values_list("product", flat=True))
    if len(all_collection_product) > 12:
        all_collection_product = all_collection_product[:12]
    category = TopCategory.objects.first()

    context = {
        "collection": collection,
        "all_collection_product": all_collection_product,
        "category": category.category.all()[1:] if category else None,
        "default_category": category.category.first() if category else None,
    }
    return render(request, "index.html", context)


def search(request):
    q = request.GET.get("q")
    product_obj = Product.objects.filter(name__icontains=q)
    category_list = Category.objects.all()
    context = {"product_obj": product_obj, "category_list": category_list, "q": q}
    return render(request, "product-list.html", context)
